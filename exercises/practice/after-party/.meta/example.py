from after_party import on_guest_list

def main():
    # Example guest list
    guest_list = ["Brad Pitt", "Selena Gomez", "Bradley Cooper"]

    # Ask user for the first name
    name_to_check = input("Enter a first name: ").strip()

    # Check the guest list using on_guest_list function
    if on_guest_list(guest_list, name_to_check):
        print(f"{name_to_check} is on the guest list!")
    else:
        print(f"{name_to_check} is NOT on the guest list.")

if __name__ == "__main__":
    main()
