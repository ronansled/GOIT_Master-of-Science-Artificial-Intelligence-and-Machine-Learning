def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            # Наприклад: недостатньо аргументів або неправильний формат
            return "Give me name and phone please."
        except KeyError:
            # Коли шукаємо контакт, якого немає в словнику
            return "Contact not found."
        except IndexError:
            # Коли користувач не передав аргумент(и) взагалі
            return "Enter user name."
    return inner


def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts):
    # Тут може виникнути ValueError/IndexError при розпакуванні
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args  # IndexError/ValueError, якщо аргументів мало
    if name not in contacts:
        # Явно провокуємо KeyError, щоб його обробив декоратор
        raise KeyError(name)
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]  # IndexError, якщо не передали ім'я
    if name not in contacts:
        raise KeyError(name)
    return f"{name}: {contacts[name]}"


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


if __name__ == "__main__":
    main()
