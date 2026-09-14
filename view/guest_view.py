class GuestView:
    def display_guest_details(self, guest):
        print("\nGuest Details")
        print("-" * 30)
        print(f"ID: {guest.guest_id}")
        print(f"Name: {guest.name}")
        print(f"Phone: {guest.phone}")
        print(f"Email: {guest.email}")

    def get_guest_input(self):
        guest_id = input("Enter guest ID: ")
        name = input("Enter guest name: ")
        phone = input("Enter guest phone: ")
        email = input("Enter guest email: ")
        return guest_id, name, phone, email

    def display_message(self, message):
        print(message)
