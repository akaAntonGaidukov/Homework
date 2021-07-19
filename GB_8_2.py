# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class only_positive(Exception):
    def __init__(self, a):
        self.a = a


result = lambda x, y: x * y if y > 0 else only_positive('Please enter only positive numbers!')

while input("To quit enter q, else enter any key.") != "q":

    print(result(int(input('Enter any number: ')), int(input('Enter only positive number: '))))
