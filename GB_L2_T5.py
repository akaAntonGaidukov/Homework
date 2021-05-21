# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


Rating = int(input("Enter a rating value: "))

rating_list = [7, 5, 3, 3, 2]

if Rating in rating_list:
    i = rating_list.index(Rating)
    rating_list.insert(i, Rating)

else:
    rating_list.append(Rating)

print(rating_list)
