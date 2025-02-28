def on_guest_list(guest_list, person):
    for name in guest_list:
        if name == person:
            return True
    return False
