# These tests are aligned with example data for the "After Party" challenge.
# Adjust or expand as needed for your specific requirements.

import unittest

from after_party import on_guest_list


class AfterPartyTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(on_guest_list([], "Brad"))

    def test_name_missing(self):
        guests = ["Brian May", "Bryn Harrison", "Albert Einstein"]
        self.assertFalse(on_guest_list(guests, "Brad"))

    def test_name_present(self):
        guests = ["Brian May", "Brad Pitt", "Albert Einstein"]
        self.assertTrue(on_guest_list(guests, "Brad"))

    def test_similar_name_not_match(self):
        guests = ["Brian May", "Bradley Cooper", "Albert Einstein"]
        self.assertFalse(on_guest_list(guests, "Brad"))

    def test_double_barrelled(self):
        guests = ["Brian May", "Brad Pitt", "Derk-Jan Karrenbeld", "Albert Einstein"]
        self.assertTrue(on_guest_list(guests, "Derk-Jan"))

    def test_single_name_person(self):
        guests = ["Cher", "Brian May", "Brad Pitt", "Albert Einstein"]
        self.assertTrue(on_guest_list(guests, "Cher"))

    def test_cheryl_instead_of_cher(self):
        guests = ["Cher", "Brian May", "Brad Pitt", "Albert Einstein"]
        self.assertFalse(on_guest_list(guests, "Cheryl"))


if __name__ == "__main__":
    unittest.main()
