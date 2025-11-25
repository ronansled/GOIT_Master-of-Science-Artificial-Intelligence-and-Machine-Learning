import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min < max <= 1000):
        return []
    if not (0 < quantity <= (max - min + 1)):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

print(get_numbers_ticket(1, 10, 5))      
print(get_numbers_ticket(10, 5, 3)) # [] — тут мін більший за макс
print(get_numbers_ticket(1, 1000, 1001)) # тут більше чисел, ніж доступно
