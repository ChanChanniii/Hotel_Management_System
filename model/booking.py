class Booking:
    def __init__(self, booking_id, guest_name, room_number, nights, total_amount):
        self.booking_id = booking_id
        self.guest_name = guest_name
        self.room_number = room_number
        self.nights = nights
        self.total_amount = total_amount
        self.status = "Confirmed"

    def __str__(self):
        return (
            f"Booking ID: {self.booking_id}\n"
            f"Guest: {self.guest_name}\n"
            f"Room: {self.room_number}\n"
            f"Nights: {self.nights}\n"
            f"Total: ${self.total_amount}\n"
            f"Status: {self.status}"
        )
