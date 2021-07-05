# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("task5.txt", "w", encoding="utf-8") as numbers:
    print("1 2 3 4 5 6 7 8 9 10", file=numbers)

with open("task5.txt", "r", encoding="utf-8") as numbers:
    num_list = numbers.read().split()

    try:
        print(f"Sum of all numbers in file is - {sum(map(lambda n : int(n), num_list))}.")
    except ValueError:
        print("Bad data Err!")
