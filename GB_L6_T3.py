# Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    # attribute
    name = "LUPA"
    last_name = "PUPKIN"
    position = "WORKER"
    _income = {"wage": 20000, "bonus": 300}


class Position(Worker):

    def get_full_name(self):
        print(f"{self.name} {self.last_name}")

    def get_total_income(self):
        print(f"Total income - {sum(self._income.values())}")


worker = Position()

worker.get_full_name()
worker.get_total_income()
