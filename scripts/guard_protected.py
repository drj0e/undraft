#!/usr/bin/env python3
"""Keep direct pushes to main inside the files the routines are allowed to write.

The writer, reviewer, and scout routines push straight to main, and the writer
and scout follow prompt files that live in this repo (docs/routines/). Both
also read the open web. So a page with instructions hidden in it could, in
principle, get a routine to rewrite the next routine's prompt, a script, or the
site's templates, and the change would take effect on the next run with nobody
having reviewed it. Each prompt forbids touching those files; this makes the
rule mechanical.

The rule: a commit that reaches main without a merged pull request may only
touch the paths the routines legitimately write (ALLOWED below). Anything else
has to arrive through a PR. Offending commits are reverted and Joe gets an
issue. Joe's own edits to protected files go through a PR too.

Usage (in CI, on push to main):
  guard_protected.py <before-sha> <after-sha>            check only
  guard_protected.py <before-sha> <after-sha> --revert   check, revert, report
Needs GITHUB_TOKEN and GITHUB_REPOSITORY for the pull-request lookup.
Exit 0 clean, 1 on a violation, 2 when a commit couldn't be verified.
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

# What a routine may change with a direct push: posts (the writer adds one, the
# reviewer and the veto workflow edit front matter), and the four logs.
ALLOWED = re.compile(
    r"^(?:blog/content/posts/[^/]+\.md"
    r"|docs/review-log\.md"
    r"|docs/tag-taxonomy\.md"
    r"|docs/inbox-log\.md"
    r"|docs/topic-backlog\.md)$"
)
ZERO = "0" * 40


def is_allowed(path):
    return bool(ALLOWED.match(path))


def violations(files_by_commit, from_merged_pr):
    """Commits that touch a protected path without a merged PR behind them.

    `files_by_commit` maps sha -> changed paths; `from_merged_pr` maps sha ->
    True/False, or None when the lookup failed. Returns (bad, unverified):
    bad is [(sha, [protected paths])], unverified is [sha] for commits that
    touch protected paths but whose PR status couldn't be read.
    """
    bad, unverified = [], []
    for sha, paths in files_by_commit.items():
        protected = [p for p in paths if not is_allowed(p)]
        if not protected:
            continue
        merged = from_merged_pr.get(sha)
        if merged is None:
            unverified.append(sha)
        elif not merged:
            bad.append((sha, protected))
    return bad, unverified


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True,
                          text=True).stdout


def commits_in_push(before, after):
    try:
        if before != ZERO:
            git("cat-file", "-e", f"{before}^{{commit}}")
            return git("rev-list", "--reverse", f"{before}..{after}").split()
    except subprocess.CalledProcessError:
        pass  # force push or unknown base: judge the head commit alone
    return [after]


def changed_paths(sha):
    # Against the first parent, so a PR merge commit shows the PR's whole diff
    # (diff-tree -m lists every parent's diff, which blames a merge for files
    # that came from main).
    parents = git("rev-list", "--parents", "-n", "1", sha).split()[1:]
    if parents:
        out = git("diff", "--name-only", parents[0], sha)
    else:
        out = git("diff-tree", "--no-commit-id", "--name-only", "-r", "--root", sha)
    return sorted({p for p in out.splitlines() if p})


def came_from_merged_pr(sha):
    repo, token = os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_TOKEN")
    if not repo or not token:
        return None
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/commits/{sha}/pulls",
        headers={"Authorization": f"Bearer {token}",
                 "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            pulls = json.load(r)
    except Exception:
        return None
    return any(p.get("merged_at") for p in pulls)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    revert = "--revert" in sys.argv
    if len(args) != 2:
        sys.exit("usage: guard_protected.py <before> <after> [--revert]")
    before, after = args
    shas = commits_in_push(before, after)
    files = {s: changed_paths(s) for s in shas}
    touched = [s for s in shas if any(not is_allowed(p) for p in files[s])]
    merged = {s: came_from_merged_pr(s) for s in touched}
    bad, unverified = violations({s: files[s] for s in touched}, merged)

    if not bad and not unverified:
        print(f"guard: {len(shas)} commit(s), all within the routine allowlist or from a merged PR")
        return 0
    for sha, paths in bad:
        print(f"UNREVIEWED: {sha[:12]} changed protected files without a merged PR: {', '.join(paths)}")
    for sha in unverified:
        print(f"UNVERIFIED: {sha[:12]} touches protected files; could not look up its pull request")

    if revert and bad:
        # Newest first, so later commits come off before the ones they build on.
        order = {s: i for i, s in enumerate(shas)}
        for sha, _ in sorted(bad, key=lambda b: -order[b[0]]):
            parents = git("rev-list", "--parents", "-n", "1", sha).split()[1:]
            cmd = ["revert", "--no-edit"] + (["-m", "1"] if len(parents) > 1 else []) + [sha]
            try:
                git(*cmd)
                print(f"reverted {sha[:12]}")
            except subprocess.CalledProcessError as e:
                subprocess.run(["git", "revert", "--abort"], capture_output=True)
                print(f"COULD NOT REVERT {sha[:12]}: {e.stderr.strip()[:300]}")
                return 1
    return 1 if bad else 2


if __name__ == "__main__":
    sys.exit(main())
