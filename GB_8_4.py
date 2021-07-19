# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class OfficeEquipment:
    ''' office equipment '''

    def __init__(self, model, price, dpi, paper_size):
        self._model = model
        self._price = price
        self._dpi = dpi
        self._paper_size = paper_size

    @property
    def model(self):
        return self._model


class Printer(OfficeEquipment):
    ''' Printer '''

    def __init__(self, model, price, dpi, paper_size, jet_type):
        self.jet_type = jet_type
        super().__init__(model, price, dpi, paper_size)


class Scanner(OfficeEquipment):
    ''' Scanner '''


class Copier(OfficeEquipment):
    ''' copying machine '''

    def __init__(self, model, price, dpi, paper_size, print_speed, monthly_print_volume):
        self.print_speed = print_speed
        self.monthly_print_volume = monthly_print_volume
        super().__init__(model, price, dpi, paper_size)


class Warehouse:
    ''' warehouse '''
    __equipments = dict()
    __issued_equipments = dict()

    def add_Equipment(self, key, value):

        if self.__equipments.get(key) == None:
            self.__equipments[key] = 0
        self.__equipments[key] += value

    def issue_Equipment(self, key, value):

        rest = self.__equipments.get(key)
        if rest != None and rest >= value:
            self.__equipments[key] -= value
            if self.__equipments[key] == 0:
                del self.__equipments[key]

    def num(self, key):
        value = self.__equipments.get(key)
        return value if value != None else 0

    def equipments_in_warehouse(self):
        print('\n------------------------------------\nLeft in warehouse:\n------------------------------------')
        for i in self.__equipments:
            print(f'{models[i].model} - {self.num(i)} pc.')
        print('------------------------------------')

    def issued_equipments(self):

        print(f'\nIssued to office:\n{self.__equipments}')


# список моделей оргтехники
models = [Printer('HP Laserjet 2130', 1950, '4800x1200', 'A4', 'laserjet'),
          Printer('CANON Pixma MG3640S BK', 3640, '4800x1200', 'A4', 'inkjet'),
          Copier('XEROX CopyCentre C118', 87800, '600x600', 'A3', 18, 10000),
          Scanner('EPSON Perfection V19', 5110, '4800×4800', 'A3')]

warehouse = Warehouse()
warehouse.equipments_in_warehouse()

while True:
    # меню операций
    print('\n -Menu- \n<1> Import.\n<2> Export.\n<Enter> Exit.')
    action = input('> ')
    if action in ['1', '2']:  # если выбрана операция
        # формируем список оргтехники
        s = ''
        for i, eq in enumerate(models):
            s += f'\n<{i}> {eq.model} ({warehouse.num(i)} pc.)'
        # меню оргтехники
        while True:
            print(f'\nEnter office equipment and amount of it:{s}')
            # выбираем модель
            try:
                model = int(input('model > '))
                if model in range(len(models)):
                    # вводим кол-во
                    n = int(input('pieces > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Value error! Enter a number from <0> to <{len(models)}>.')
                continue
            else:
                # совершаем операцию
                print('\nexchanging:')
                if (action == '1'):  # принимаем технику на склад
                    print(f'Accepted to warehouse {models[model].model} - {n} pc.')
                    warehouse.add_Equipment(model, n)
                elif (action == '2'):  # выдаём технику со склада
                    max = warehouse.num(model)
                    if (n > max):  # если запрошено больше, чем есть
                        n = max
                        print(f'Caution! Only {n} left!. {models[model].model}!')
                    print(f'exported from warehouse {models[model].model} - {n} pc.')
                    warehouse.issue_Equipment(model, n)

                # выводим остатки по складу
                warehouse.equipments_in_warehouse()
                break

            if (input('\nPress <Enter> to continue or any key to exit...') != ''):
                break
    elif action == '':  # если выбран выход - завершаем работу
        break
    else:
        print('Wrong value entered. please chose between <1> or <2>.')