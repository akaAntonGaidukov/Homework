# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

inpt = int(input("Enter type in seconds here, to change it to HH:MM:SS format - "))

# Calculating Hours, Min, and Sec.
H = inpt // 3600
M = (inpt - (H*3600))//60
S = (inpt - (H*3600) - (M*60))

# Printing time in new format. * {var:02d} used to show 2 digit numbers *
print(f"Time in new format: {H:02d}:{M:02d}:{S:02d}")
