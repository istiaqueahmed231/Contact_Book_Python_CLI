# main.py
from contact_operations import (
    Add_Contact, Save_as_txt, load_from_csv,
    delete_from_list, search_contact
)

contact_list = []
contact_list = load_from_csv(contact_list)

print(".....Welcome to Contact Book Management System.....")
while True:
    print("\n<<<<< MENU >>>>>")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Export as CSV")
    print("4. Remove a Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Select Option >>> ")

    if choice == "6":
        Save_as_txt(contact_list)
        print("Contacts saved. Exiting...")
        break

    elif choice == "1":
        contact_list = Add_Contact(contact_list)
        Save_as_txt(contact_list)

    elif choice == "2":
        if contact_list:
            for c in contact_list:
                print(c)
        else:
            print("No contacts available.")

    elif choice == "3":
        Save_as_txt(contact_list)
        print("Contacts saved to all_contacts.csv.")

    elif choice == "4":
        contact_list = delete_from_list(contact_list)
        Save_as_txt(contact_list)

    elif choice == "5":
        search_contact(contact_list)

    else:
        print("Invalid choice. Try again.")
