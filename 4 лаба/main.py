import re

def command_array(command, array):
    index = re.match(r"Получить элемент по (\d+) индексу", command)
    range = re.match(r"Получить элементы с (\d+) по (\d+) шагом (\d+)", command)
    end = re.match(r"Получить (\d+) элемент с конца", command)

    if index:
        idx = int(index.group(1)) - 1
        if idx < 0 or idx >= len(array):
            return "Ошибка: индекс выходит за пределы массива"
        return array[idx]

    if range:
        start_idx = int(range.group(1)) - 1
        end_idx = int(range.group(2)) - 1
        step = int(range.group(3))
        if start_idx < 0 or end_idx < 0 or start_idx >= len(array) or end_idx >= len(array):
            return "Ошибка: некорректные границы массива"
        return array[start_idx:end_idx + 1:step]

    if end:
        n = int(end.group(1))
        if n < 1 or n > len(array):
            return "Ошибка: индекс выходит за пределы массива"
        return array[-n]

    return "Ошибка: команда не распознана"

array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Текущий массив: {array}")

print('\nДля выполнения программы введите команду:')
print('1. Получить элемент по n индексу')
print('2. Получить элементы с n по b шагом v')
print('3. Получить n элемент с конца')
print('Введите "выход", чтобы завершить программу')


while True:
    user_input = input("\nВведите команду: ")
    if user_input.lower() == 'выход':
        break
    result = command_array(user_input, array)
    print(f"Результат: {result}")
