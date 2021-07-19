# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.

class exception(Exception):
    def __init__(self, a):
        self.a = a



my_list = []

while True:
    my_data = input("Enter number: ")
    if my_data == "":
        break
    try:
        if my_data.replace("-", "").replace(".", "").isdigit():
            my_list.append(float(my_data))
        else:
            raise exception("Not a number!")
    except exception as err:
        print(err)
    continue

print(f"Entered numbers - {my_list}")
