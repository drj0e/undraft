#!/usr/bin/env python3
"""Tests for the reach pacing and backlog parsing in check_diversity.py."""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_diversity import allowed_reach, load_backlog


class AllowedReach(unittest.TestCase):
    def test_three_core_in_a_row_forces_a_step_out(self):
        self.assertEqual(allowed_reach(["core"] * 3), {"adjacent", "new"})

    def test_unlabeled_history_counts_as_core(self):
        self.assertEqual(allowed_reach([None, None, None]), {"adjacent", "new"})

    def test_a_recent_branch_allows_core_again(self):
        self.assertEqual(allowed_reach(["core", "adjacent", "core"]),
                         {"core", "adjacent", "new"})

    def test_new_at_most_once_in_six(self):
        # 'new' four posts back still blocks another; six back does not.
        self.assertNotIn("new", allowed_reach(["new", "core", "adjacent", "core"]))
        self.assertIn("new", allowed_reach(["new", "core", "core", "adjacent", "core", "core"]))

    def test_both_limits_at_once_leave_adjacent(self):
        self.assertEqual(allowed_reach(["new", "core", "core", "core"]), {"adjacent"})

    def test_short_history_is_unconstrained(self):
        self.assertEqual(allowed_reach(["core", "core"]), {"core", "adjacent", "new"})


class LoadBacklog(unittest.TestCase):
    def test_parses_items_and_status(self):
        text = (
            "# Topic Backlog\n\n## Items\n\n"
            "### B-2026-09-27-1 | adjacent | open\n"
            "- added: 2026-09-27\n- thesis: Postmortems are a data model.\n\n"
            "### B-2026-09-27-2 | new | used: some-slug\n"
            "- added: 2026-09-27\n- thesis: Something else.\n"
        )
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(text)
        try:
            items = load_backlog(f.name)
        finally:
            os.unlink(f.name)
        self.assertEqual([i["id"] for i in items], ["B-2026-09-27-1", "B-2026-09-27-2"])
        self.assertEqual(items[0]["reach"], "adjacent")
        self.assertEqual(items[0]["status"], "open")
        self.assertEqual(items[0]["added"], "2026-09-27")
        self.assertEqual(items[0]["thesis"], "Postmortems are a data model.")
        self.assertEqual(items[1]["status"], "used: some-slug")

    def test_missing_file_is_empty(self):
        self.assertEqual(load_backlog("/nonexistent/backlog.md"), [])


if __name__ == "__main__":
    unittest.main()
