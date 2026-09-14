from model.guest import Guest


class GuestController:
    def __init__(self, repository, view):
        self.repository = repository
        self.view = view

    def add_guest(self):
        guest_id, name, phone, email = self.view.get_guest_input()
        guest = Guest(guest_id, name, phone, email)
        self.repository.add_guest(guest)
        self.view.display_message(f"Guest {name} added successfully.")
        self.view.display_guest_details(guest)

    def list_guests(self):
        guests = self.repository.get_all_guests()
        if not guests:
            self.view.display_message("No guests found.")
            return

        for guest in guests:
            self.view.display_guest_details(guest)
