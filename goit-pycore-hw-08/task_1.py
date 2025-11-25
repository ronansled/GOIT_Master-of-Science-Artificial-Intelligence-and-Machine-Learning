import pickle
from datetime import datetime, timedelta


# ===== FIELD CLASSES =====

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Birthday must be in format DD.MM.YYYY")
        super().__init__(value)


# ===== RECORD =====

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str):
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.phones.append(Phone(new_phone))
                return
        raise ValueError("Phone not found.")

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = self.birthday.value if self.birthday else "N/A"
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}"


# ===== ADDRESS BOOK =====

class AddressBook(dict):
    def add_record(self, record: Record):
        self[record.name.value] = record

    def find(self, name: str):
        return self.get(name)

    def delete(self, name: str):
        if name in self:
            del self[name]

    def upcoming_birthdays(self, days=7):
        today = datetime.today().date()
        upcoming = []
        for record in self.values():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                bday_this_year = bday.replace(year=today.year)
                if 0 <= (bday_this_year - today).days <= days:
                    upcoming.append(record)
        return upcoming


# ===== DATA SAVE / LOAD =====

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            book = pickle.load(f)
            print("✅ Дані відновлено з файлу.")
            return book
    except FileNotFoundError:
        print("📂 Створено нову адресну книгу.")
        return AddressBook()


# ===== COMMAND PROCESSING =====

def parse_input(user_input):
    parts = user_input.split()
    return parts[0], parts[1:]


def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record:
        record.add_phone(phone)
        save_data(book)
        return "Phone added to existing contact."
    else:
        new_record = Record(name)
        new_record.add_phone(phone)
        book.add_record(new_record)
        save_data(book)
        return "Contact created."


def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        save_data(book)
        return "Phone updated."
    return "Contact not found."


def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return str(record)
    return "Contact not found."


def show_all(book):
    if not book:
        return "No contacts saved."
    return "\n".join(str(rec) for rec in book.values())


def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        save_data(book)
        return "Birthday added."
    return "Contact not found."


def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return record.birthday.value
    return "Birthday not found."


def birthdays(args, book):
    upcoming = book.upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(str(rec) for rec in upcoming)


# ===== MAIN LOOP =====

def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
