import sys
from pathlib import Path

def print_directory_structure(path: Path, prefix: str = ""):
    """
    Рекурсивно виводить структуру директорії без кольорів.
    Директорії позначені 📂, файли – 📜.
    """
    if not path.exists():
        print(f"Помилка: шлях '{path}' не існує.")
        return
    if not path.is_dir():
        print(f"Помилка: шлях '{path}' не є директорією.")
        return

    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        branch = "┗ " if is_last else "┣ "

        if item.is_dir():
            print(f"{prefix}{branch}📂 {item.name}/")
            # рекурсивний виклик для піддиректорії
            new_prefix = prefix + ("   " if is_last else "┃  ")
            print_directory_structure(item, new_prefix)
        else:
            print(f"{prefix}{branch}📜 {item.name}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
        print("Приклад: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])
    print(f"📦 {dir_path.name}")
    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()

