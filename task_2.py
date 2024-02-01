def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # Знайшли точний елемент, шукаємо перший елемент, що більший або рівний target
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]  # Поточний mid може бути верхньою межею
            right = mid - 1

    if upper_bound is None and left < len(arr):
        # Якщо не знайдено точного співпадіння, але є елементи праворуч від останнього перевіреного
        upper_bound = arr[left]

    return iterations, upper_bound


# Тестування функції
arr = [0.1, 0.5, 1.3, 2.4, 3.9, 4.8]
target = 2.5
iterations, upper_bound = binary_search_with_upper_bound(arr, target)
print(f"Iterations: {iterations}, Upper Bound: {upper_bound}")
