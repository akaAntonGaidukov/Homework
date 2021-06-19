# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил A километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее B километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

fdd = float(input("Enter how many kilometers runner traveled on his first day: "))   # First Day Distance in KM     (A)
rd = int(input("Enter how many kilometers is his goal: "))    # Result Distance in KM         (B)
d = 1  # Days

while fdd <= rd:
    fdd = fdd * 1.1
    d += 1

print(f"On {d} - day, runner reached his goal and ran {round(fdd)} km")
