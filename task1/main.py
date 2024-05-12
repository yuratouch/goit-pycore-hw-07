import re
from collections import UserDict

class PhoneVerificationError(Exception):
    def __init__(self, phone):
        self.phone = phone
        self.message = f"Invalid phone number: {phone}"
        super().__init__(self.message)

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        self.name = Field(name)

class Phone(Field):
    pattern = r'\d{10}$'

    def __init__(self, phone):
        super().__init__(phone)
        if re.match(Phone.pattern, phone):
            self.phone = phone
        else:
             raise PhoneVerificationError(phone)
         
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except PhoneVerificationError as e: 
            print(e.message)

    def remove_phone(self, phone):
        self.phones.remove(self.find_phone(phone)) 

    def edit_phone(self, old, new):
        for index in range(len(self.phones)):
            if self.phones[index].phone == old:
                self.phones[index] = Phone(new)

    def find_phone(self, phone_input):
        for phone in self.phones:
            if phone_input == phone.phone:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def find(self, name):
        for record_name, record in self.data.items():
            if name == record_name.name.value:
                return record
            
    def delete(self, name):
        for record_name, record in self.data.items():
            if name == record_name.name.value:
                self.data.pop(record_name)
                break

        
        
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
