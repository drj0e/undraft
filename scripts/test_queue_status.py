#!/usr/bin/env python3
"""Tests for the writer's queue/date planner (queue_status.plan)."""
import datetime as dt
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from queue_status import MIN_LEAD, plan

D = dt.date.fromisoformat
TODAY = D("2026-09-28")


class Plan(unittest.TestCase):
    def test_empty_queue_honours_lead_floor(self):
        # The failure this exists for: latest post is today, so "latest + 2"
        # would give a two-day veto window.
        allowed, queued, skip = plan([D("2026-09-24"), D("2026-09-27")], TODAY)
        self.assertIsNone(skip)
        self.assertEqual(queued, [])
        self.assertTrue(all((d - TODAY).days >= MIN_LEAD for d in allowed))

    def test_normal_queue_uses_gap_and_skips_repeat_gap(self):
        # latest is 6 days out with a 3-day gap before it: 3 is excluded.
        dates = [D("2026-10-01"), D("2026-10-04")]
        allowed, _, skip = plan(dates, TODAY)
        self.assertIsNone(skip)
        self.assertEqual(allowed, [D("2026-10-06"), D("2026-10-08")])

    def test_full_queue_skips(self):
        dates = [D("2026-09-30"), D("2026-10-03"), D("2026-10-06")]
        allowed, queued, skip = plan(dates, TODAY)
        self.assertEqual(allowed, [])
        self.assertEqual(len(queued), 3)
        self.assertIn("queue full", skip)

    def test_held_posts_are_not_in_dates(self):
        # load() drops draft: true; a held post must not count as queued.
        allowed, queued, _ = plan([D("2026-09-27")], TODAY)
        self.assertEqual(queued, [])
        self.assertTrue(allowed)


if __name__ == "__main__":
    unittest.main()
