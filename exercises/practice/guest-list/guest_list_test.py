# These tests are generated based on test data from the problem specification 
# https://github.com/exercism/website/tree/main/bootcamp_content/projects/string-puzzles/exercises/guest-list

import unittest
from guest_list import on_guest_list


class GuestListTest(unittest.TestCase):
    def test_person_is_on_a_single_person_list(self):
        expected = True
        self.assertEqual(on_guest_list(["Jeremy"], "Jeremy"), expected)

    def test_person_is_not_on_a_single_person_list(self):
        expected = False
        self.assertEqual(on_guest_list(["Nicole"], "Jeremy"), expected)

    def test_person_is_on_a_larger_guest_list(self):
        expected = True
        self.assertEqual(on_guest_list(["Aron", "Jeremy", "Nicole"], "Jeremy"), expected)

    def test_person_is_not_on_a_larger_guest_list(self):
        expected = False
        self.assertEqual(on_guest_list(["Aron", "Frank", "Nicole"], "Jeremy"), expected)

    def test_guest_list_is_empty(self):
        expected = False
        self.assertEqual(on_guest_list([], "Jeremy"), expected)

    def test_guest_list_with_duplicate_names(self):
        expected = True
        self.assertEqual(on_guest_list(["Jeremy", "Jeremy"], "Jeremy"), expected)

    def test_case_sensitivity(self):
        expected = False  # Assuming names must match exactly (case-sensitive)
        self.assertEqual(on_guest_list(["jeremy"], "Jeremy"), expected)

    def test_checking_a_different_name(self):
        expected = False
        self.assertEqual(on_guest_list(["Aron", "Frank", "Nicole"], "Alex"), expected)

