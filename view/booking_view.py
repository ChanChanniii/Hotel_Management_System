class BookingView:
    def get_booking_input(self):
        guest_name = input("Enter guest name: ")
        room_number = input("Enter room number: ")
        nights = int(input("Enter number of nights: "))
        return guest_name, room_number, nights

    def get_cancel_booking_id(self):
        return int(input("Enter booking ID to cancel: "))

    def display_booking(self, booking):
        print("\nBooking Details")
        print("-" * 30)
        print(booking)

    def display_bookings(self, bookings):
        if not bookings:
            print("No bookings available.")
            return

        print("\nCurrent Reservations")
        print("-" * 40)
        for booking in bookings:
            print(f"Booking ID: {booking.booking_id} | Guest: {booking.guest_name} | Room: {booking.room_number} | Nights: {booking.nights} | Total: ${booking.total_amount}")

    def display_message(self, message):
        print(message)
