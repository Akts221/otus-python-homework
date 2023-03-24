"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return[numb**2 for numb in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    list_numbers = []
    if filter_type == ODD:
        return [num for num in numbers_list if num % 2 != 0]
    elif filter_type == EVEN:
        return [num for num in numbers_list if num % 2 == 0]
    elif filter_type == PRIME:
        for num in numbers_list:
            flag = False
            if num == 1:
                flag = True
            elif num > 1:
                for num_1 in range(2, num):
                    if (num % num_1) == 0:
                        flag = True
                if not flag:
                    list_numbers.append(num)
        return list_numbers

