# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

User_string = input("Enter a sentence devided by blank spaces: ").split(" ")

for ind, el in enumerate(User_string, 1):
    print(f"{ind})  {el}") if len(el) < 10 else print(f"{ind})  {el[:10]}")
