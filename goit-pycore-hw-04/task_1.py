def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Обрізаємо пробіли і символи нового рядка
                line = line.strip()
                if not line:  # Пропускаємо порожні рядки
                    continue
                try:
                    name, salary = line.split(',')
                    salary = float(salary)  # перетворюємо зарплату у число
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Пропущено некоректний рядок: {line}")
        if count == 0:
            average = 0
        else:
            average = total / count
        return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
        return 0, 0

total, average = total_salary("task_1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

