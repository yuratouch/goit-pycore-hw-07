from input_parser import parse_input
from flie_handler import save_to_file, get_contacts
from contacts_handler import add_contact, change_contact, show_phone, show_all

def main():
    contacts = get_contacts()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_to_file(contacts)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            save_to_file(contacts)
            print(show_all())

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
