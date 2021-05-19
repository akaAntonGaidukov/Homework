# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input("Enter a number here: "))

maxval = 0

while 0 != num:
    n = num % 10
    if maxval < n:
        maxval = n
    num = num//10

print(maxval)
