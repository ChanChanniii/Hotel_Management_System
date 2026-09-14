class LoginView:
    def show_login_menu(self):
        print("\n=== Hotel Management Login ===")
        print("Default accounts:")
        print("- admin / admin123")
        print("- staff / staff123")

    def get_login_input(self):
        username = input("Username: ")
        password = input("Password: ")
        return username, password

    def display_message(self, message):
        print(message)
