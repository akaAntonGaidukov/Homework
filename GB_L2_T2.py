# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

List = input("Enter values separated by space bar: ").split(" ")

List_length = len(List) if len(List) % 2 == 0 else (len(List)-1)
List[:List_length:2], List[1:List_length:2] = List[1:List_length:2], List[:List_length:2]

print(List)
