# 1. Запросите у пользователя значения выручки и издержек фирмы.
# 2. Определите, с каким финансовым результатом работает фирма.
# 3. Если фирма отработала с прибылью, вычислите рентабельность выручки.
#  Это отношение прибыли к выручке.
# 4. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

profit = int(input("Enter how much profit did your company made: "))
expenses = int(input("Enter how much did it cost: "))

currency = "$"
margin = profit / expenses
clean_profit = profit - expenses

if clean_profit > 0:
    print(f"Your company is profitable. Your profits are {clean_profit} {currency}, and your margin is {round(margin, 2)}")
    workers = int(input("How many employees work for you?"))
    print(f"On average each worker makes {round((clean_profit / workers), 2)} {currency}")
elif clean_profit == 0:
    print("Your company is making zero profits!")
else:
    print("Your company is not profitable!")
