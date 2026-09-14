from model.credential import Credential


class LoginController:
    def __init__(self, view):
        self.view = view
        self.users = [
            Credential("admin", "admin123", "admin"),
            Credential("staff", "staff123", "staff"),
        ]

    def login(self):
        username, password = self.view.get_login_input()

        for user in self.users:
            if user.matches(username, password):
                self.view.display_message(f"Login successful! Welcome, {user.role}.")
                return user.role

        self.view.display_message("Invalid username or password.")
        return None
