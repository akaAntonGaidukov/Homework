# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def sum_f():
    """This function sums all values entered to quit it you must enter a special character (Q)"""
    ans = 0
    while True:
        in_input = input("To exit the program enter Q.\n"
                         "Enter numbers separated by blank space: ").split()
        try:

            for el in in_input:
                if el == "Q" or el == "q":
                    return ans
                else:
                    ans+=int(el)

        except ValueError as err:
            sep = "*"*50
            print(f"{sep}\n{err}\n try again please!\n{sep}")

        print(f"Sum of entered numbers is - {ans}")


print(sum_f())