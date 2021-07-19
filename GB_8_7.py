# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __str__(self):
        return f'{self.real}+{self.img}i' if self.img > 0 else f'{self.real}{self.img}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.img * other.img),
                             (self.img * other.real + self.real * other.img))


cn_1 = ComplexNumber(3, -1)
cn_2 = ComplexNumber(6, 5)
print(cn_1 + cn_2)
print(cn_1 * cn_2)
print(complex(7, -4) * complex(2, 2))
