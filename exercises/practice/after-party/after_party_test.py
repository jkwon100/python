# These tests are auto-generated with test data from:
# https://github.com/exercism/website/blob/main/bootcamp_content/projects/string-puzzles/exercises/after-party/config.json
# File last updated on 2024-02-28

import unittest
from after_party import (
    on_guest_list,
)


class AfterPartyTest(unittest.TestCase):
    def test_empty_list(self):
        """
        slug: empty-list
        description: No-one's allowed in
        name: Empty register
        """
        candidates, name_to_check = [], "Brad"
        expected = False
        self.assertEqual(on_guest_list(candidates, name_to_check), expected)

    def test_name_missing(self):
        """
        slug: name-missing
        description: The name's not on the list
        name: Brad's turned away
        """
        candidates = ["Brian May", "Bryn Harrison", "Albert Einstein"]
        name_to_check = "Brad"
        expected = False
        self.assertEqual(on_guest_list(candidates, name_to_check), expected)

    def test_name_present(self):
        """
        slug: name-present
        description: The name's on the list
        name: Brad's allowed in
        """
        candidates = ["Brian May", "Brad Pitt", "Albert Einstein"]
        name_to_check = "Brad"
        expected = True
        self.assertEqual(on_guest_list(candidates, name_to_check), expected)

    def test_similar_name(self):
        """
        slug: similar-name
        description: The name isn't on the list
        name: Close, not nope
        """
        candidates = ["Brian May", "Bradley Cooper", "Albert Einstein"]
        name_to_check = "Brad"
        expected = False
        self.assertEqual(on_guest_list(candidates, name_to_check), expected)

    def test_double_barrelled(self):
        """
        slug: double-barrelled
        description: The name's on the list, but it's hyphenated
        name: A dutchman
        """
        candidates = [
            "Brian May",
            "Brad Pitt",
            "Derk-Jan Karrenbeld",
            "Albert Einstein"
        ]
        name_to_check = "Derk-Jan"
        expected = True
        self.assertEqual(on_guest_list(candidates, name_to_check), expected)

    def test_cher(self):
        """
        slug: cher
        description: Some people only have one name
        name: Cher's in town
        """
        candidates = ["Cher", "Brian May", "Brad Pitt", "Albert Einstein"]
        name_to_check = "Cher"
        expected = True
        self.assertEqual(on_guest_list(candidates, name_to_check), expected)

    def test_cheryl(self):
        """
        slug: cheryl
        description: Are Cheryl Crow and Cher friends?
        name: Getting tough now
        """
        candidates = ["Cher", "Brian May", "Brad Pitt", "Albert Einstein"]
        name_to_check = "Cheryl"
        expected = False
        self.assertEqual(on_guest_list(candidates, name_to_check), expected)


if __name__ == "__main__":
    unittest.main()
