from cli.services.file_service import write_contacts_to_file, read_contacts_from_file
from cli.utils.helpers import parse_input
from cli.services.command_service import add_contact, change_contact, get_phone, get_all_contacts, add_birthday, \
    show_birthday, search, add_address, add_email, add_phone, get_birthdays, delete_contact
from cli.models.address_book import AddressBook


def main():
    book = AddressBook()
    book_from_file = read_contacts_from_file("book.pkl")
    if book_from_file is not None:
        book = book_from_file
    print("Welcome to the assistant bot!")
    print("""
        Command list:
        'hello' - shows hello message
        ---
        'add <name>' - adds a new contact. Arguments birthday, address and email are not required.
        'add-phone <name> <phone>' - adds a new phone number
        'add-birthday <name> <birthday_date>' - adds a birthday
        'add-address <name> <address>' - adds an address
        'add-email <name> <email>' - adds an email
        ---
        'change <name> <old_phone> <phone>' - changes a phone number in the contact
        ---
        'phone <name>' - get all phone numbers in the contact
        'all' - get all contacts
        'birthdays <days_in_advance>' - shows all birthdays in the next days in advance. <days_in_advance> is not required.
        'show-birthday <name>' - shows a birthday
        ---
        'delete <name>' - delete contact from the contact
        'search <search_query>' - for searching information in the contact
        ---
        'exit' or 'close' - closes the app
    """)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Hi! How can I help you?")
        elif command == "add":
            print(add_contact(args, book=book))
        elif command == "add-phone":
            print(add_phone(args, book=book))
        elif command == "add-birthday":
            print(add_birthday(args, book=book))
        elif command == "add-address":
            print(add_address(args, book=book))
        elif command == "add-email":
            print(add_email(args, book=book))
        elif command == "change":
            print(change_contact(args, book=book))
        elif command == "phone":
            print(get_phone(args, book=book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "show-birthday":
            print(show_birthday(args, book=book))
        elif command == "birthdays":
            print(get_birthdays(book=book, days_in_advance=args[0] if args else None))
        elif command == "search":
            print(search(args, book=book))
        elif command == "delete":
            print(delete_contact(args, book=book))
        else:
            print("Invalid command.")

        write_contacts_to_file("book.pkl", book)


if __name__ == "__main__":
    main()
