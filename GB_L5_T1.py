# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

file = open("task1.txt", "w", encoding="utf-8")

while True:

    imp = input("To exit this program press enter with a blank line\nPlease enter your data:")
    if imp == "":
        break

    print(imp, file=file)

file.close()
