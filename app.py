def display_menu():
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("This contact already exists!")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("Your contact book is empty.")
        return
    print("\nSaved Contacts:")
    for name, info in contacts.items():
        print(f"- {name}: {info['Phone']} | {info['Email']}")

def search_contact(contacts):
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nFound Details for {name}:")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 4.")

if __name__ == "__main__":
    main()