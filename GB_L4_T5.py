# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

new_l_multiple = [num for num in range(100, 1001, 2)]


def my_func(prev_el, el):
    return prev_el + el


print(reduce(my_func, new_l_multiple))
