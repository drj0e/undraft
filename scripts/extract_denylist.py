#!/usr/bin/env python3
"""Pull the terms out of the _undraft-denylist doc's exported text.

The doc is a Google Doc, and the Drive tools read it back as markdown: the
`---` separator comes out as `\\---`, underscores as `\\_`, and blank lines
carry stray spaces. A literal match on `---` finds nothing, which silently
turns the inbox off (writer) or holds every inbox post (reviewer). This
undoes the export's escaping and trims, then prints one term per line.

  extract_denylist.py <doc-text-file> > /tmp/denylist.txt

Exit 1 when the separator is missing or no terms follow it: callers treat
that as "no denylist", never as "nothing is banned".
"""
import re
import sys

SEPARATOR = re.compile(r"^\s*\\?-{3,}\s*$")


def terms(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if SEPARATOR.match(line):
            break
    else:
        return None  # no separator: not a denylist we can trust
    out = []
    for line in lines[i + 1:]:
        term = re.sub(r"\\(.)", r"\1", line).strip()  # undo markdown escapes
        term = term.lstrip("-*•").strip() if re.match(r"^[-*•]\s", term) else term
        if term and term not in out:
            out.append(term)
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: extract_denylist.py <doc-text-file>")
    with open(sys.argv[1], encoding="utf-8") as f:
        found = terms(f.read())
    if found is None:
        print("no --- separator in the denylist text", file=sys.stderr)
        return 1
    if not found:
        print("the denylist has no terms below its --- line", file=sys.stderr)
        return 1
    print("\n".join(found))
    return 0


if __name__ == "__main__":
    sys.exit(main())
