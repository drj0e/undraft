#!/usr/bin/env python3
"""Tests for extract_denylist.py against what Google Docs exports look like."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_denylist import terms

# Shape of a real read_file_content export of the denylist doc: escaped
# separator, space-only lines between paragraphs.
EXPORT = "Header text.\n\n  \n\nOne term per line.\n\n  \n\n\\---\n\n  \n"


class Terms(unittest.TestCase):
    def test_escaped_separator_from_a_google_doc(self):
        # The bug this exists for: `\---` never matched a literal `---`.
        self.assertEqual(terms(EXPORT + "\nAcme\n\n  \n\nWidget Hub\n"), ["Acme", "Widget Hub"])

    def test_plain_separator_still_works(self):
        self.assertEqual(terms("x\n---\nAcme\n"), ["Acme"])

    def test_markdown_escapes_and_whitespace_are_undone(self):
        self.assertEqual(terms("---\n  field\\_name  \nA\\*B\n"), ["field_name", "A*B"])

    def test_bullets_are_stripped(self):
        self.assertEqual(terms("---\n- Acme\n* Widget Hub\n"), ["Acme", "Widget Hub"])

    def test_empty_or_missing_list_is_not_an_empty_ban(self):
        self.assertEqual(terms(EXPORT), [])
        self.assertIsNone(terms("no separator here\nAcme\n"))

    def test_duplicates_collapse(self):
        self.assertEqual(terms("---\nAcme\nacme\nAcme\n"), ["Acme", "acme"])


if __name__ == "__main__":
    unittest.main()
