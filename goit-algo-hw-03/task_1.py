import os
import shutil
import argparse


def copy_and_sort_files(src_dir, dest_dir):
    """
    Рекурсивно перебирає всі файли у src_dir, копіює їх у dest_dir
    і сортує у піддиректорії за розширенням файлу. Уникає перезапису файлів.
    """
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            
            if os.path.isdir(src_path):
                copy_and_sort_files(src_path, dest_dir)
            elif os.path.isfile(src_path):
                ext = os.path.splitext(item)[1][1:] or "no_extension"
                target_dir = os.path.join(dest_dir, ext)
                os.makedirs(target_dir, exist_ok=True)
                
                target_path = os.path.join(target_dir, item)
                
                # Перевірка на існування і генерація унікального імені
                base_name, extension = os.path.splitext(item)
                counter = 1
                while os.path.exists(target_path):
                    target_path = os.path.join(target_dir, f"{base_name}_{counter}{extension}")
                    counter += 1
                
                try:
                    shutil.copy2(src_path, target_path)
                    print(f"Файл {src_path} скопійовано у {target_path}")
                except Exception as e:
                    print(f"Помилка при копіюванні {src_path}: {e}")
    except Exception as e:
        print(f"Помилка при доступі до директорії {src_dir}: {e}")



def main():
    parser = argparse.ArgumentParser(description="Копіювання та сортування файлів за розширенням")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    
    args = parser.parse_args()
    src_dir = args.src
    dest_dir = args.dest
    
    if not os.path.exists(src_dir):
        print(f"Вихідна директорія {src_dir} не існує.")
        return

    os.makedirs(dest_dir, exist_ok=True)
    copy_and_sort_files(src_dir, dest_dir)
    print("Копіювання та сортування завершено.")

if __name__ == "__main__":
    main()
