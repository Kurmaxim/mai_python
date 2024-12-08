# Изучите модуль itertools в Python. Напишите программу, которая использует этот модуль для решения следующих задач:

# Создание бесконечного генератора чисел. 
# Применение функций к каждому элементу в итераторе.
# Объединение нескольких итераторов в один.
# Используйте функции и методы из модуля itertools, чтобы выполнить указанные задачи.
# Убедитесь, что ваш скрипт может обрабатывать исключения, связанные с отсутствием данных в итераторах.

import itertools

def generator(size, start=0, step=1):
    numbers = []
    generator = itertools.count(start, step)
    for _ in range(size):
        numbers.append(next(generator))
    return numbers


def apply_function(function, iterable):
    if isinstance(iterable, (list, tuple)):
        return type(iterable)(apply_function(function, item) if isinstance(item, (list, tuple)) else function(item) for item in iterable)
    else:
        return function(iterable)

def combine_iterators(*iterables):
    return list(itertools.chain(*iterables))

def combine_iterators_in_iterator(iterable):
    return list(itertools.chain.from_iterable(iterable))

print(combine_iterators_in_iterator(apply_function(lambda x: x**2, [generator(5, -10, 2.5), generator(3)])))
print(apply_function(lambda x: x * 2, combine_iterators(generator(5, -10, 2.5), generator(3), generator(10, 0, 5))))
print(combine_iterators_in_iterator(apply_function(lambda x: x**2, [generator(0), generator(0)])))
print(apply_function(lambda x: x * 2, combine_iterators(generator(0), generator(0), generator(0))))