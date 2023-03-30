"""Design a class ‘Complex ‘with data members for real and imaginary part. Provide default and
Parameterized constructors. Write a program to perform arithmetic operations of two complex
numbers."""


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def show(self):
        print(f"Complex Number: {self.real} + {self.imag}i")

    @staticmethod
    def add(r1, r2, i1, i2):
        real = r1 + r2  # adding real parts
        imaginary = i1 + i2  # adding imaginary parts
        print(f"Sum of Two Complex Numbers is: {real} + {imaginary}i")

    @staticmethod
    def sub(r1, r2, i1, i2):
        real = r1 - r2  # subtracting real parts
        imaginary = i1 - i2  # subtracting imaginary parts
        print(f"Subtraction of Two Complex Numbers is: {real} + {imaginary}i")


ob1 = Complex(2, 4)
ob2 = Complex(3, 4)

ob1.show()
ob2.show()
print()
Complex.add(ob1.real, ob2.real, ob1.imag, ob2.imag)
Complex.sub(ob1.real, ob2.real, ob1.imag, ob2.imag)
