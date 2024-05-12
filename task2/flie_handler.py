from datetime import datetime
from book import AddressBook, Record

def save_to_file(book: AddressBook) -> None:  
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for record_name, record in book.data.items():
            line = record_name.value + " " + ','.join(p.value for p in record.phones)

            if record.birthday:
                file.write(line + " " + datetime.strftime(record.birthday.birthday, "%d.%m.%Y") + "\n")   
            else:
                file.write(line + "\n") 

def save_phones(list, record):
    if len(list) > 0:
        for phone in list:
            record.add_phone(phone)

def get_contacts() -> AddressBook:
    book = AddressBook()
    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                try:
                    name, phone_numbers, date = line.split()
                    record = Record(name)

                    save_phones(phone_numbers.split(","), record)
                    record.add_birthday(date)
                    book.add_record(record)

                except ValueError:
                    name, phone_numbers = line.split()
                    record = Record(name)

                    save_phones(phone_numbers.split(","), record)
                    book.add_record(record)

            return book
        
    except FileNotFoundError:
        return book