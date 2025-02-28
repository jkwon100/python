from after_party import on_guest_list

def on_guest_list(guest_list, first_name):
    """Return True if 'first_name' exactly matches the first token of any full name in 'guest_list'."""
    return any((guest.split()[0] if guest else "") == first_name for guest in guest_list)
