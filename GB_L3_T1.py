# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devi(dev, det):
    while True:
        try:
            x = (int(dev) / (int(det)))
            return x
        except ZeroDivisionError:
            print("Please don`t be stupid like this")
            dev = int(input("enter divident: "))
            det = int(input("enter divisor: "))
            continue

d1 = int(input("enter divident: "))
d2 = int(input("enter divisor: "))
print(f"{d1}/{d2}={devi(d1,d2)}")
