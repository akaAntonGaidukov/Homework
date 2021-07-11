# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
"""ENTER ( PATH >python GB_L4_T1 *args ) in terminal"""
name, working_hours, payment_hours, bonus = argv

print(f"Paycheck: {(int(working_hours)*int(payment_hours))+int(bonus)}$")
