import unittest
from after_party import on_guest_list

class AfterPartyTest(unittest.TestCase):
    
    def test_person_is_on_guest_list(self):
        guest_list = ["Brad Pitt", "Selena Gomez", "Bradley Cooper"]
        self.assertTrue(on_guest_list(guest_list, "Brad"))
        self.assertTrue(on_guest_list(guest_list, "Selena"))
        self.assertTrue(on_guest_list(guest_list, "Bradley"))
    
    def test_person_is_not_on_guest_list(self):
        guest_list = ["Brad Pitt", "Dwayne Johnson"]
        self.assertFalse(on_guest_list(guest_list, "Tom"))
        self.assertFalse(on_guest_list(guest_list, "Sel"))
    
    def test_empty_guest_list(self):
        guest_list = []
        self.assertFalse(on_guest_list(guest_list, "Brad"))
        self.assertFalse(on_guest_list(guest_list, "Dwayne"))
    
    def test_multiple_names_same_first_name(self):
        guest_list = ["Brad Pitt", "Bradley Cooper", "Brad Monk"]
        # Should be True because all begin with "Brad"
        self.assertTrue(on_guest_list(guest_list, "Brad"))
        self.assertTrue(on_guest_list(guest_list, "Bradley"))
    
    def test_person_on_longer_list(self):
        guest_list = [
            "Angelina Jolie",
            "Brad Pitt",
            "Chris Hemsworth",
            "Dwayne Johnson",
            "Natalie Portman"
        ]
        self.assertTrue(on_guest_list(guest_list, "Brad"))
        self.assertFalse(on_guest_list(guest_list, "Chrissy"))

if __name__ == "__main__":
    unittest.main()
