# contact_model.py

def User_Info(User_Name, User_Email, User_Phone, User_address):
    return {
        "name": User_Name,
        "email": User_Email,
        "phone": User_Phone,
        "address": User_address
    }

def check_phone_number(contacts_list, entered_number):
    for m in contacts_list:
        if m["phone"] == entered_number:
            print(f"The phone number is already entered with contact '{m['name']}'.")
            print("Enter another phone number to proceed.")
            return 0
    return 1
