# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(words_list):
    capitalized = "New text: "
    for word in words_list:
        c = 0
        for letters in word:
            if 65 <= ord(letters) <= 122:
                c += 1
        if c == len(word):
            cap = word.capitalize()
            capitalized += str(cap) + " "

    print(capitalized)


words = input("enter a word to capitalize it: ").split()

int_func(words)
