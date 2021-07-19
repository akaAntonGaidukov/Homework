# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count
from itertools import cycle
from time import sleep

start_num = int(input("Enter a starting value for counter: "))
count_list = []

for el in count(start_num):
    if el > start_num+10:
        break
    count_list.append(el)
print(count_list)

sleep(2)

c = 0
for el in cycle(["green", "yellow", "red", "yellow"]):
    if c > 10:
        break
    print(el)
    sleep(1)
    c += 1
