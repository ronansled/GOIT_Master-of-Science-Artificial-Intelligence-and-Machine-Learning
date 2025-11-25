def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change [name] [phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Contact '{name}' not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

# -------------------------------
# Тестовий блок
# -------------------------------
def run_tests():
    contacts = {}
    assert add_contact(["John", "12345"], contacts) == "Contact added."
    assert contacts["John"] == "12345"

    assert add_contact(["Alice", "67890"], contacts) == "Contact added."
    assert contacts["Alice"] == "67890"

    assert show_phone(["John"], contacts) == "John: 12345"
    assert show_phone(["Bob"], contacts) == "Contact 'Bob' not found."

    assert change_contact(["John", "54321"], contacts) == "Contact updated."
    assert contacts["John"] == "54321"

    assert change_contact(["Bob", "11111"], contacts) == "Contact 'Bob' not found."

    all_contacts = show_all(contacts)
    expected_output = "John: 54321\nAlice: 67890"
    assert all_contacts == expected_output

    print("All tests passed!")

if __name__ == "__main__":
    # Виконати тести, якщо скрипт запускається з аргументом "test"
    import sys
    if len(sys.argv) > 1 and sys.argv[1].lower() == "test":
        run_tests()
    else:
        main()
