import timeit
import random


# -----------------------------
# 1. Сортування вставками
# -----------------------------
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# -----------------------------
# 2. Сортування злиттям
# -----------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -----------------------------
# 3. Timsort (вбудоване sorted)
# -----------------------------
def timsort(arr):
    return sorted(arr)


# -----------------------------
# 4. Додаткове завдання:
#    merge_k_lists — об'єднання k відсортованих списків
# -----------------------------
def merge_k_lists(lists):
    if not lists:
        return []

    result = lists[0]
    for i in range(1, len(lists)):
        result = merge(result, lists[i])  # використовуємо merge з merge sort
    return result


# -----------------------------
# 5. Емпіричне порівняння алгоритмів
# -----------------------------
def benchmark():
    sizes = [1000, 5000, 10000]

    print("\n=== ЕМПІРИЧНЕ ПОРІВНЯННЯ АЛГОРИТМІВ ===")

    for n in sizes:
        data = [random.randint(0, 100000) for _ in range(n)]
        print(f"\n--- Розмір масиву: {n} ---")

        t_insertion = timeit.timeit(lambda: insertion_sort(data), number=1)
        print(f"Insertion Sort: {t_insertion:.4f} сек.")

        t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
        print(f"Merge Sort: {t_merge:.4f} сек.")

        t_timsort = timeit.timeit(lambda: timsort(data), number=1)
        print(f"Timsort (sorted): {t_timsort:.4f} сек.")


# -----------------------------
# 6. Демонстрація роботи
# -----------------------------
def demo_examples():
    print("\n=== ПРИКЛАДИ РОБОТИ АЛГОРИТМІВ ===")

    data = [12, 4, 7, 1, 9, 3]
    print("\nПочатковий список:", data)

    print("Insertion Sort:", insertion_sort(data))
    print("Merge Sort:", merge_sort(data))
    print("Timsort:", timsort(data))

    print("\n=== ДОДАТКОВЕ ЗАВДАННЯ ===")

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Вхідні списки:", lists)
    print("Об'єднаний відсортований список:", merged_list)


# -----------------------------
# 7. Запуск програми
# -----------------------------
if __name__ == "__main__":
    benchmark()
    demo_examples()
