def hanoi(n, source, target, auxiliary, rods):
    """
    Рекурсивне переміщення n дисків зі стрижня source на стрижень target
    з використанням допоміжного стрижня auxiliary.
    
    rods: словник зі списками дисків на кожному стрижні
    """
    if n == 1:
        disk = rods[source].pop()
        rods[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {rods}")
    else:
        # Перемістити n-1 дисків на допоміжний стрижень
        hanoi(n-1, source, auxiliary, target, rods)
        # Перемістити останній диск на цільовий стрижень
        hanoi(1, source, target, auxiliary, rods)
        # Перемістити n-1 дисків з допоміжного на цільовий
        hanoi(n-1, auxiliary, target, source, rods)

def main():
    try:
        n = int(input("Введіть кількість дисків (ціле число >=1): "))
        if n < 1:
            raise ValueError
    except ValueError:
        print("Помилка: введіть ціле число >=1")
        return
    
    # Ініціалізація стрижнів
    rods = {
        'A': list(range(n, 0, -1)),  # [n, n-1, ..., 1]
        'B': [],
        'C': []
    }
    
    print(f"Початковий стан: {rods}")
    hanoi(n, 'A', 'C', 'B', rods)
    print(f"Кінцевий стан: {rods}")

if __name__ == "__main__":
    main()
