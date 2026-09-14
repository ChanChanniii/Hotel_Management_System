class Guest:
    def __init__(self, guest_id, name, phone, email):
        self.guest_id = guest_id
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Guest {self.guest_id}: {self.name} ({self.email})"
