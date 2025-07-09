import json
import os
FILE_NAME = "contacts.txt"
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file)
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print(" Contact added successfully.\n")
def view_contacts(contacts):
    if not contacts:
        print(" No contacts found.\n")
        return
    print("\n Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()
def edit_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= idx < len(contacts):
            contacts[idx]['name'] = input("Enter new name: ")
            contacts[idx]['phone'] = input("Enter new phone number: ")
            contacts[idx]['email'] = input("Enter new email address: ")
            print(" Contact updated successfully.\n")
        else:
            print(" Invalid contact number.\n")
    except ValueError:
        print(" Please enter a valid number.\n")
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= idx < len(contacts):
            deleted = contacts.pop(idx)
            print(f" Contact '{deleted['name']}' deleted successfully.\n")
        else:
            print(" Invalid contact number.\n")
    except ValueError:
        print(" Please enter a valid number.\n")
def main():
    contacts = load_contacts()
    while True:
        print(" Contact Management Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1–5): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print(" Contacts saved. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.\n")
main()
