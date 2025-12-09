def binary_search_with_upper_bound(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] >= x:
            upper_bound = arr[mid]         # можливий кандидат
            right = mid - 1               # шукаємо менший елемент
        else:
            left = mid + 1

    return iterations, upper_bound

###-- Тестові приклади --###
arr = [0.5, 1.2, 2.3, 3.3, 4.8, 5.0, 7.4]
x = 5.0

result = binary_search_with_upper_bound(arr, x)
print(result)

arr2 = [-2.5, -1.1, 0.0, 0.9, 1.7, 3.14, 6.28]
x2 = 7.0

print(binary_search_with_upper_bound(arr2, x2))

arr = [0.1, 0.5, 1.0, 1.5, 2.2, 3.8, 5.0, 7.7]
x = 6.0

print(binary_search_with_upper_bound(arr, x))

