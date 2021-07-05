# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("task3.txt", "r", encoding="utf-8") as info:
    data_list = info.readlines()
    data_dict = {}
    for i in data_list:
        i = i.rstrip("\n")
        kw, val = i.split()
        if float(val) < 20000:
            print(f"{kw}, earns less than 20k RUB.")
        data_dict.update({kw: float(val)})

    print(f"\nAverage paycheck is about ~ {sum(data_dict.values()) / len(data_dict)} RUB.")
