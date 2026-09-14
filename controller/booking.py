from model.booking import Booking


class BookingController:
    def __init__(self, repository):
        self.repository = repository

    def create_booking(self, guest_name, room_number, nights):
        room = self.find_room(room_number)
        if room is None:
            return None, "Room not found."
        if not room.available:
            return None, "Room is already booked."

        room.mark_booked()
        booking_id = len(self.repository.get_all_bookings()) + 1
        total_amount = room.price_per_night * nights
        booking = Booking(booking_id, guest_name, room_number, nights, total_amount)
        self.repository.add_booking(booking)
        self.log_transaction(f"BOOKED | Guest: {guest_name} | Room: {room_number} | Nights: {nights} | Total: ${total_amount}")
        return booking, "Booking created successfully."

    def cancel_booking(self, booking_id):
        for booking in self.repository.get_all_bookings():
            if booking.booking_id == booking_id:
                room = self.find_room(booking.room_number)
                if room is not None:
                    room.mark_available()

                self.repository.bookings.remove(booking)
                self.log_transaction(f"CANCELLED | Booking ID: {booking_id} | Guest: {booking.guest_name} | Room: {booking.room_number}")
                return True, "Reservation cancelled successfully."

        return False, "Booking ID not found."

    def find_room(self, room_number):
        for room in self.repository.get_all_rooms():
            if str(room.room_number) == str(room_number):
                return room
        return None

    def list_bookings(self):
        return self.repository.get_all_bookings()

    def log_transaction(self, message):
        with open("transaction.txt", "a", encoding="utf-8") as file:
            file.write(message + "\n")
