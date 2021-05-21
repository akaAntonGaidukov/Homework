# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

Month = input("Enter a numeral for month: ")

month_name = ["january", "february", "march", "april", "may", "june", "july",
              "august", "september", "october", "november", "december"]

seasons_dict = {"winter": "12,1,2", "spring": "3,4,5", "summer": "6,7,8", "autumn": "9,10,11"}

for key, value in seasons_dict.items():
    if Month in value.split(","):
        print(f"{month_name[int(Month)-1].capitalize()} is {key.capitalize()}")
