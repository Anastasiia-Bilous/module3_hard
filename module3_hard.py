def calculate_structure_sum(data_structure):
    total_sum = 0  #  задаём значение переменной 0
    for elem in data_structure: #  перебор каждого элемента
        if isinstance(elem, int):  # если элемент - число
            total_sum += elem  #   суммируем число
        elif isinstance(elem, str):  # если элемент - строка
            total_sum += len(elem)  # суммируем длину строки
        elif isinstance(elem, list) or isinstance(elem, tuple): # если элемент - списока или кортеж
            total_sum += calculate_structure_sum(elem)  # рекурсия для распаковки списков или кортежей
        elif isinstance(elem, dict):  # если элемент - словарь
            total_sum += calculate_structure_sum(list(elem.keys()))  # рекурсия словарь - ключи
            total_sum += calculate_structure_sum(list(elem.values()))  # рекурсия словарь - значения
        elif isinstance(elem, set):  # если злемент - множество
            total_sum += calculate_structure_sum(elem)  # рекурсия для распаковки множества
    return total_sum  #  возврат общей суммы

# Входные данные:
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)