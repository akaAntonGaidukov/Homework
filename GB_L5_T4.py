# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator
translator = Translator()


with open("task4.txt", "r", encoding="utf-8") as info:
    data_list = info.readlines()
    translated = []
    for i in data_list:
        i = i.rstrip("\n")
        tr = (translator.translate(i, dest='ru'))
        translated.append(tr.text)

with open("task4_T.txt", "w", encoding="utf-8") as translated_file:
    for txt in translated:
        print(txt, file=translated_file)
