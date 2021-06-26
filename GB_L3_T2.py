# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def info(name, last_name, date, city, email, phone):
    print(f" Name - {name} Last name - {last_name} Date of birth - {date} City of birth - {city} "
          f"Email - {email} Phone number - {phone}")

n,ln,d,c,e,p,*other = str(input("enter name, last name, date of birth, city of birth, email,"
                 " and phone number of user separated by blank space( ): ")).split(" ")

info(name=n, last_name=ln, date=d, city=c, email=e, phone=p)
