Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time
import random

... # Генерация массива случайных чисел
... data = [random.randint(1, 100) for _ in range(10000)]
... 
... # Функция для быстрой сортировки
... def quicksort_descending(nums):
...     if len(nums) <= 1:
...         return nums
...     pivot = nums[len(nums) // 2]
...     greater = [n for n in nums if n > pivot]
...     equal = [n for n in nums if n == pivot]
...     smaller = [n for n in nums if n < pivot]
...     return quicksort_descending(greater) + equal + quicksort_descending(smaller)
... 
... # Функция для пузырьковой сортировки (по убыванию)
... def bubblesort_descending(nums):
...     length = len(nums)
...     for i in range(length):
...         for j in range(length - i - 1):
...             if nums[j] < nums[j + 1]:
...                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
...     return nums
... 
... # Создание независимых копий исходного массива
... data_for_quick = data[:]
... data_for_bubble = data[:]
... 
... # Замер времени выполнения быстрой сортировки
... start = time.time()
... sorted_quick = quicksort_descending(data_for_quick)
... quick_time = time.time() - start
... 
... # Замер времени выполнения пузырьковой сортировки
... start = time.time()
... sorted_bubble = bubblesort_descending(data_for_bubble)
... bubble_time = time.time() - start
... 
... # Вывод результатов времени работы
... print(f"Быстрая сортировка заняла: {quick_time:.2f} секунд")
... print(f"Пузырьковая сортировка заняла: {bubble_time:.2f} секунд")
