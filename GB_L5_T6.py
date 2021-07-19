# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.

# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   -   10(лаб)
#                                         Физкультура:   -   30(пр)   -
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

with open("task6.txt", "r", encoding="utf-8") as data:
    courses = []
    hours = []
    while True:
        line = data.readline()
        try:
            c, h = line.split(":")
            courses.append(c)
            hours_filter = h.split()
            clean_hours = []
            for d in hours_filter:
                f = re.sub("[^0-9]", "", d)
                if f != "":
                    clean_hours.append(int(f))

            hours.append(clean_hours)
        except ValueError:
            pass

        if not line:
            break
    schedule = map(lambda c, h: {c :sum(h)}, courses, hours)
    print("Your schedule dictionary is below\n")
    print(*schedule)


