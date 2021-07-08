# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(number):
    for i in range(1, number + 1):
        factorial = 1
        for num in range(1, i+1):
            factorial *= num
        yield factorial


n = int(input("enter a number: "))

count = (num for num in range(1, n+1))


for facts in fact(n):
    print(f"Factorial of {next(count)} is {facts}.")
