def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:  # пропускаємо порожні рядки
                    continue
                try:
                    cat_id, name, age = line.split(',')
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_list.append(cat_dict)
                except ValueError:
                    print(f"Пропущено некоректний рядок: {line}")
        return cats_list
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
        return []


cats_info = get_cats_info("task_2.txt")
for cat in cats_info:
    print(cat)
