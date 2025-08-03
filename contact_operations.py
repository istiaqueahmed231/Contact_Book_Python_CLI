# contact_operations.py
import time,csv
from contact_model import User_Info, check_phone_number

def Add_Contact(contact_list):
    while True:
        name = input("Enter Name: ")
        if any(ch.isdigit() for ch in name):
            print("Name can't contain digits. Try again.")
            continue
        break

    email = input("Enter Email Address: ")

    while True:
        phone = input("Enter Phone Number: ")
        if phone.isdigit():
            if check_phone_number(contact_list, phone) != 0:
                break
        else:
            print("Phone number must only contain digits (0-9).")

    address = input("Enter Address: ")
    print("Saving contact...")
    time.sleep(1)
    contact_list.append(User_Info(name, email, phone, address))
    return contact_list

def Save_as_txt(contact_list):
    with open("all_contacts.csv", "w", encoding="utf-8") as fp:
        fp.write("Name,Email,Phone,Address\n")
        for book in contact_list:
            line = f"{book['name']},{book['email']},{book['phone']},{book['address']}\n"
            fp.write(line)

def load_from_csv(contact_list):
    try:
        with open("all_contacts.csv", "r", encoding="utf-8") as pf:
            reader = csv.reader(pf)
            header = next(reader)  # skip the header line
            for row in reader:
                if len(row) < 4:
                    continue  # skip malformed lines
                name, email, phone, address = row[0], row[1], row[2], ",".join(row[3:])
                contact_list.append({
                    "name": name.strip(),
                    "email": email.strip(),
                    "phone": phone.strip(),
                    "address": address.strip(),
                })
    except FileNotFoundError:
        pass
    return contact_list

def delete_from_list(contact_list):
    rem = input("Enter the name of the contact to be removed: ")
    for contact in contact_list:
        if contact["name"] == rem:
            contact_list.remove(contact)
            print(f"Contact '{rem}' removed successfully.")
            return contact_list
    print("Contact not found.")
    return contact_list

def search_contact(contact_list):
    print("1. Search by Name")
    print("2. Search by Email")
    print("3. Search by Phone")
    print("4. Search by Address")
    print("5. Back")
    choice = input("Select option >>> ")

    if choice == "1":
        term = input("Enter part of the name: ").lower()
        found = False
        for contact in contact_list:
            if term in contact["name"].lower():
                print("Contact found:", contact)
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "2":
        term = input("Enter part of the email: ").lower()
        found = False
        for contact in contact_list:
            if term in contact["email"].lower():
                print("Contact found:", contact)
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "3":
        term = input("Enter part of the phone number: ")
        found = False
        for contact in contact_list:
            if term in contact["phone"]:
                print("Contact found:", contact)
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        term = input("Enter part of the address: ").lower()
        found = False
        for contact in contact_list:
            if term in contact["address"].lower():
                print("Contact found:", contact)
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "5":
        return
