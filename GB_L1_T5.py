# 1. Запросите у пользователя значения выручки и издержек фирмы.
# 2. Определите, с каким финансовым результатом работает фирма.
# 3. Если фирма отработала с прибылью, вычислите рентабельность выручки.
#  Это отношение прибыли к выручке.
# 4. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

profit = int(input("Enter how much profit did your company made: "))
expence = int(input("Enter how much did it cost: "))

cleanprofit = profit-expence
if cleanprofit > 0:
    print(f"Your company is profitable. Your profits are {cleanprofit}")
    workers = int(input("How many employees work for you?"))
    print(f"On average each worker makes {round((cleanprofit/workers),2)}")
else:
    print("Your company is not profitable")
