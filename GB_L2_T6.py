# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

inventory_tuple_list = []
i = 1
while True:
    try:
        inventory_tuple_list.append(
        (input('Enter id: '), dict({
            'name': str(input('Enter name: ')),
            'price': float(input('Enter price in dollars: ')),
            'quantity': int(input('Enter quantity: ')),
            'units': str(input('Enter in what units you defy quantity ')),
        }))
    )
    except ValueError:
        pass

    if input('inventory has been updated. Add another item? Y/N: ') == 'N':
        break

    i += 1

print(f'Inventory: {inventory_tuple_list}')

output_dict = dict({})
for product in inventory_tuple_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})


print(f'Analytics: {output_dict}')

