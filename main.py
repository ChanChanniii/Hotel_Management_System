from controller.booking import BookingController
from controller.guest import GuestController
from controller.login import LoginController
from model.file_repository import FileRepository
from model.room import Room
from view.booking_view import BookingView
from view.guest_view import GuestView
from view.login_view import LoginView


def main():
    repository = FileRepository()
    guest_view = GuestView()
    booking_view = BookingView()
    login_view = LoginView()

    repository.add_room(Room(1, 101, "Single", 60, True))
    repository.add_room(Room(2, 102, "Double", 90, True))
    repository.add_room(Room(3, 103, "Suite", 150, False))

    guest_controller = GuestController(repository, guest_view)
    booking_controller = BookingController(repository)
    login_controller = LoginController(login_view)

    login_view.show_login_menu()
    role = login_controller.login()

    if role is None:
        print("Access denied. Exiting program.")
        return

    while True:
        print("\n" + "=" * 70)
        print("                 HORIZON HOTEL & SUITES")
        print("=" * 70)
        print("Welcome back! Find your perfect stay.")
        print("\nQuick actions:")
        print("1. Search Rooms")
        print("2. Create Booking")
        print("3. Add Guest")
        print("4. View Guests")
        print("5. View Bookings")
        print("6. Cancel Reservation")
        print("7. Booking Deals")
        print("8. Exit")
        print("=" * 70)

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nAvailable Rooms")
            for room in repository.get_all_rooms():
                print(f"- Room {room.room_number} | {room.room_type} | ${room.price_per_night}/night | {'Available' if room.available else 'Booked'}")
        elif choice == "2":
            guest_name, room_number, nights = booking_view.get_booking_input()
            booking, message = booking_controller.create_booking(guest_name, room_number, nights)
            booking_view.display_message(message)
            if booking:
                booking_view.display_booking(booking)
        elif choice == "3":
            guest_controller.add_guest()
        elif choice == "4":
            guest_controller.list_guests()
        elif choice == "5":
            booking_view.display_bookings(booking_controller.list_bookings())
        elif choice == "6":
            booking_id = booking_view.get_cancel_booking_id()
            status, message = booking_controller.cancel_booking(booking_id)
            booking_view.display_message(message)
            if status:
                booking_view.display_bookings(booking_controller.list_bookings())
        elif choice == "7":
            print("\nFeatured Offers")
            print("- Weekend Escape: 15% off deluxe rooms")
            print("- Family Stay: Free breakfast for 2 kids")
            print("- Business Deal: Complimentary Wi-Fi and parking")
        elif choice == "8":
            print("Thank you for choosing Horizon Hotel. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
