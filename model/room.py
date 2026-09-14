class Room:
    def __init__(self, room_id, room_number, room_type, price_per_night, available=True):
        self.room_id = room_id
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.available = available

    def mark_booked(self):
        self.available = False

    def mark_available(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Booked"
        return f"Room {self.room_number} ({self.room_type}) - {status} - ${self.price_per_night}/night"
