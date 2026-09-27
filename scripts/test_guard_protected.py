#!/usr/bin/env python3
"""Tests for guard_protected.py: the allowlist, the verdicts, and real git."""
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guard_protected as g


class Allowlist(unittest.TestCase):
    def test_routine_paths_are_allowed(self):
        for p in ("blog/content/posts/a-post.md", "docs/review-log.md",
                  "docs/tag-taxonomy.md", "docs/inbox-log.md",
                  "docs/topic-backlog.md"):
            self.assertTrue(g.is_allowed(p), p)

    def test_instructions_code_and_site_are_protected(self):
        for p in ("docs/routines/writer.md", "claude.md", "scripts/lint_posts.py",
                  ".github/workflows/hugo.yml", "docs/review-checklist.md",
                  "blog/layouts/partials/footer.html", "blog/hugo.toml",
                  "blog/content/about.md", "blog/content/posts/sub/x.md",
                  "blog/content/posts/x.html", "README.md"):
            self.assertFalse(g.is_allowed(p), p)


class Violations(unittest.TestCase):
    def test_protected_change_without_pr_is_bad(self):
        bad, unv = g.violations({"a": ["docs/routines/writer.md", "docs/review-log.md"]},
                                {"a": False})
        self.assertEqual(bad, [("a", ["docs/routines/writer.md"])])
        self.assertEqual(unv, [])

    def test_merged_pr_passes(self):
        self.assertEqual(g.violations({"a": ["claude.md"]}, {"a": True}), ([], []))

    def test_failed_lookup_is_unverified_not_bad(self):
        self.assertEqual(g.violations({"a": ["claude.md"]}, {"a": None}), ([], ["a"]))

    def test_allowlisted_only_needs_no_lookup(self):
        self.assertEqual(g.violations({"a": ["docs/review-log.md"]}, {}), ([], []))


class RealGit(unittest.TestCase):
    """changed_paths / commits_in_push against an actual repository."""

    def setUp(self):
        self.old = os.getcwd()
        self.tmp = tempfile.TemporaryDirectory()
        os.chdir(self.tmp.name)
        self.run_git("init", "-q", "-b", "main")
        self.run_git("config", "user.email", "t@example.com")
        self.run_git("config", "user.name", "t")
        self.base = self.commit("docs/review-log.md", "log\n")

    def tearDown(self):
        os.chdir(self.old)
        self.tmp.cleanup()

    def run_git(self, *a):
        return subprocess.run(["git", *a], check=True, capture_output=True, text=True).stdout.strip()

    def commit(self, path, text):
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "a") as f:
            f.write(text)
        self.run_git("add", path)
        self.run_git("commit", "-q", "-m", path)
        return self.run_git("rev-parse", "HEAD")

    def test_direct_push_range_and_paths(self):
        a = self.commit("blog/content/posts/p.md", "x\n")
        b = self.commit("docs/routines/writer.md", "evil\n")
        self.assertEqual(g.commits_in_push(self.base, b), [a, b])
        self.assertEqual(g.changed_paths(b), ["docs/routines/writer.md"])

    def test_merge_commit_shows_the_branch_diff(self):
        self.run_git("checkout", "-q", "-b", "feature")
        self.commit("claude.md", "rule\n")
        self.run_git("checkout", "-q", "main")
        self.commit("docs/review-log.md", "more\n")
        self.run_git("merge", "-q", "--no-ff", "-m", "merge", "feature")
        m = self.run_git("rev-parse", "HEAD")
        self.assertEqual(g.changed_paths(m), ["claude.md"])

    def test_unknown_base_judges_head_only(self):
        head = self.commit("claude.md", "x\n")
        self.assertEqual(g.commits_in_push("f" * 40, head), [head])
        self.assertEqual(g.commits_in_push(g.ZERO, head), [head])


if __name__ == "__main__":
    unittest.main()
