def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Перевірка кешу
        if n in cache:
            return cache[n]

        # Обчислення, збереження в кеш і повернення результату
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Приклад використання
fib = caching_fibonacci()
print(fib(10)) 
print(fib(15))  