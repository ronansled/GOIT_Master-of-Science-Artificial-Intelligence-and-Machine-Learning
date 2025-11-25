import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Функція-генератор, що ітерує по всіх дійсних числах,
    чітко відокремлених пробілами з обох боків у тексті.
    """
    # Регулярний вираз для пошуку дійсних чисел з пробілами з обох сторін
    pattern = r'(?<=\s)[0-9]+\.?[0-9]*(?=\s)'
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    """
    Функція для підсумовування чисел,
    отриманих від генератора func на основі тексту.
    """
    total = 0.0
    for number in func(text):
        total += number
    return total


# Приклад використання
text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
