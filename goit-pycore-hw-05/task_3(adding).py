import sys


def parse_log_line(line: str) -> dict:
    """
    Парсить рядок логу у словник з ключами:
    date, time, level, message.
    """
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        raise ValueError("Некоректний формат рядка логу")
    date, time, level, message = parts
    return {
        'date': date,
        'time': time,
        'level': level.upper(),
        'message': message
    }


def load_logs(file_path: str) -> list:
    """
    Завантажує лог-файл, повертає список записів у вигляді словників.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    try:
                        log = parse_log_line(line)
                        logs.append(log)
                    except ValueError as e:
                        print(f"Пропуск рядка через помилку формату: {e}", file=sys.stderr)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Помилка читання файлу: {e}", file=sys.stderr)
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує записи по рівню логування, регістр не враховується.
    """
    level_upper = level.upper()
    return list(filter(lambda log: log['level'] == level_upper, logs))


def count_logs_by_level(logs: list) -> dict:
    """
    Рахує кількість записів по кожному рівню логування.
    """
    counts = {}
    for log in logs:
        lvl = log['level']
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts


def display_log_counts(counts: dict):
    """
    Виводить у вигляді таблиці кількість записів за рівнями логування.
    """
    print(f"{'Рівень логування':<17} | {'Кількість'}")
    print(f"{'-' * 17}-|{'-' * 10}")
    for level in sorted(counts.keys()):
        print(f"{level:<17} | {counts[level]}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу_логів> [рівень_логування]", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{filter_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЗаписів з рівнем '{filter_level.upper()}' не знайдено.")


# --------- Приклад перевірки без файлу ---------

example_log_text = """\
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
"""


def demo():
    print("=== Демонстрація ===")
    lines = example_log_text.strip().splitlines()
    logs = [parse_log_line(line) for line in lines]

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    level = "error"
    filtered = filter_logs_by_level(logs, level)
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in filtered:
        print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    # Для реального запуску через файл розкоментуйте:
    # main()


    demo()
