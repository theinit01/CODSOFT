import json

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        """Add a new contact."""
        name = input("Enter the contact's name: ").strip()
        if name in self.contacts:
            print("Contact already exists.")
            return

        phone = input("Enter the contact's phone number: ").strip()
        email = input("Enter the contact's email: ").strip()
        address = input("Enter the contact's address: ").strip()

        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts found.")
            return

        print("Contacts List:")
        for name, info in self.contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        search_term = input("Enter the contact's name or phone number to search: ").strip()

        found = False
        for name, info in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in info['phone']:
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
                found = True
        
        if not found:
            print("No matching contacts found.")

    def update_contact(self):
        """Update an existing contact."""
        name = input("Enter the contact's name to update: ").strip()
        if name not in self.contacts:
            print("Contact not found.")
            return

        phone = input(f"Enter the new phone number (current: {self.contacts[name]['phone']}): ").strip()
        email = input(f"Enter the new email (current: {self.contacts[name]['email']}): ").strip()
        address = input(f"Enter the new address (current: {self.contacts[name]['address']}): ").strip()

        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        self.save_contacts()
        print("Contact updated successfully!")

    def delete_contact(self):
        """Delete an existing contact."""
        name = input("Enter the contact's name to delete: ").strip()
        if name not in self.contacts:
            print("Contact not found.")
            return

        del self.contacts[name]
        self.save_contacts()
        print("Contact deleted successfully!")

    def display_menu(self):
        """Display the menu and handle user choice."""
        while True:
            print("\nContact Book Menu")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.display_menu()
