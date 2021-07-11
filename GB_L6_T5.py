# Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = "Name"

    def draw(self):
        print(f"Drawing")


class Pen(Stationery):

    def draw(self):
        print("Drawing with pen")


class Pencil(Stationery):

    def draw(self):
        print("Drawing with pencil")


class Sharpie(Stationery):

    def draw(self):
        print("Drawing with sharpie")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

sharpie = Sharpie()
sharpie.draw()

