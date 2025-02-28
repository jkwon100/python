from after_party import on_guest_list

def on_guest_list(guest_list, first_name):
    """
    Return True if 'first_name' exactly matches the first part of any name in 'guest_list'.

    Example:
      guest_list = ["Brad Pitt", "Cher", "Derk-Jan Karrenbeld"]
      first_name = "Brad"
      -> True  (since "Brad Pitt" starts with "Brad")

    If the list is empty or no match is found, return False.
    """
    for guest in guest_list:
        # Strip and split the guest's name into words
        name_parts = guest.strip().split()
        
        # If there's at least one part, check if the first one matches 'first_name'
        if name_parts and name_parts[0] == first_name:
            return True
    
    # No matches found
    return False

