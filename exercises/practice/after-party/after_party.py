def on_guest_list(guest_list, first_name):
    return any(name.startswith(first_name) for name in guest_list)