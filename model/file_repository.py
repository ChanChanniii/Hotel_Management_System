class FileRepository:
    def __init__(self):
        self.guests = []
        self.rooms = []
        self.bookings = []

    def add_guest(self, guest):
        self.guests.append(guest)

    def add_room(self, room):
        self.rooms.append(room)

    def add_booking(self, booking):
        self.bookings.append(booking)

    def get_all_rooms(self):
        return self.rooms

    def get_all_bookings(self):
        return self.bookings

    def get_guest_by_id(self, guest_id):
        for guest in self.guests:
            if str(guest.guest_id) == str(guest_id):
                return guest
        return None

    def get_all_guests(self):
        return self.guests
