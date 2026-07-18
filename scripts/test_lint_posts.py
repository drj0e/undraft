#!/usr/bin/env python3
"""Tests for the advisory self-citation checks in lint_posts.py.

These cover the deterministic surfacing layer: it cannot judge whether a
paraphrase is faithful (that's the reviewer's job), but it can (a) list every
claim a post makes about a prior post so none is skipped, and (b) flag the
precise fingerprint of the bug that motivated this work: a citing post that
enumerates a strict subset of a list in the post it links to.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lint_posts import find_self_citations, find_subset_enumerations, tic_hits


class FindSelfCitations(unittest.TestCase):
    def test_flags_first_person_claim_about_a_linked_post(self):
        body = (
            "Months back I [listed what a system needs]"
            "(/posts/the-stack/) before you let an agent run: "
            "the output has to be selectable and stoppable.\n"
        )
        hits = find_self_citations(body)
        self.assertEqual(len(hits), 1)
        self.assertIn("the-stack", hits[0])

    def test_ignores_a_plain_link_with_no_self_claim(self):
        body = "See [the guard pipeline](/posts/the-stack/) for the full ordering.\n"
        self.assertEqual(find_self_citations(body), [])


class FindSubsetEnumerations(unittest.TestCase):
    def test_flags_citing_list_that_drops_a_member_of_the_target_list(self):
        citing = (
            "Months back I [listed what a system needs](/posts/the-stack/): "
            "the output has to be selectable, constrained, audited, and stoppable.\n"
        )
        targets = {
            "the-stack": (
                "The system makes output selectable, constrainable, "
                "auditable, affordable, and stoppable.\n"
            )
        }
        hits = find_subset_enumerations(citing, targets)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["slug"], "the-stack")
        self.assertIn("affordable", hits[0]["missing"])

    def test_list_parsing_keeps_last_item_and_drops_conjunction(self):
        citing = (
            "I [listed it](/posts/the-stack/): "
            "selectable, constrained, audited, and stoppable.\n"
        )
        targets = {
            "the-stack": (
                "output is selectable, constrainable, auditable, "
                "affordable, and stoppable.\n"
            )
        }
        hit = find_subset_enumerations(citing, targets)[0]
        self.assertEqual(
            hit["citing"], ["selectable", "constrained", "audited", "stoppable"]
        )
        self.assertNotIn("and", hit["target"])
        self.assertIn("stoppable", hit["target"])

    def test_no_flag_when_citing_list_matches_target_list(self):
        citing = (
            "I [listed the properties](/posts/the-stack/): "
            "selectable, constrainable, auditable, and stoppable.\n"
        )
        targets = {
            "the-stack": (
                "The system makes output selectable, constrainable, "
                "auditable, and stoppable.\n"
            )
        }
        self.assertEqual(find_subset_enumerations(citing, targets), [])


class TicHits(unittest.TestCase):
    def test_flags_therapist_voice_and_whole_point_family(self):
        body = (
            "That loss is real and it's worth naming. Sit with that for a "
            "moment. The signature is the entire load-bearing idea, and "
            "that's the whole point.\n"
        )
        hits = tic_hits(body)
        self.assertIn("worth naming", hits)
        self.assertIn("sit with that", hits)
        self.assertIn("is the entire l", hits)
        self.assertIn("that's the whole point", hits)

    def test_you_already_know_only_in_tic_forms(self):
        # Standalone-beat and known-object forms are the tic...
        self.assertTrue(tic_hits("And the fix? You already know.\n"))
        self.assertTrue(tic_hits("You already know the answer here.\n"))
        # ...a plain relative clause is not.
        self.assertEqual(tic_hits("Use the tools you already know well.\n"), [])

    def test_clean_prose_passes(self):
        body = (
            "The migration is real work nobody funded. Naming the steward "
            "matters more than naming the tool.\n"
        )
        self.assertEqual(tic_hits(body), [])


if __name__ == "__main__":
    unittest.main()
