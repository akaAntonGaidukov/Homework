# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

sep = "-" * 50

with open("task2.txt", "a+", encoding="utf-8") as txt:
    print("three more words\n" * 2, file=txt)

    txt.seek(0)
    txt_list = txt.readlines()
    for l in range(len(txt_list)):
        try:
            if not txt_list[l+1]:
                break

            else:
                n = txt_list[l]
                wn = str(len(n.split()))
                print(" This line contains " + wn + " words - " + n, end="")
        except IndexError:
            pass

    print(f"\n{sep}\nIn total this file contains {len(txt_list)} lines.")
