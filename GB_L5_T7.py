# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
#
#                   название, форма, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.

# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

""" kyrilica + """
import json

with open("task7.txt", "r", encoding="utf-8") as data:
    name = []
    earnings = []
    list_of_dicts = []

    while True:
        line = data.readline()
        try:
            n, f, i, e = line.split()
            name.append(n)
            profit = int(i)-int(e)
            earnings.append(profit)
            dicts = {n: profit}
            list_of_dicts.append(dicts)

        except ValueError:
            pass

        if not line:
            break

profitable = {int(n) for n in earnings if n >= 0}
ap_dict = {"Averege_profit": sum(profitable)}
with open("task7_7.json", "w", encoding="utf-8") as data_w:
    json.dump(list_of_dicts, data_w, indent=2, ensure_ascii=False)
    json.dump(ap_dict, data_w, indent=2, ensure_ascii=False)


