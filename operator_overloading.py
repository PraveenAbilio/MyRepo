class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __add__(self, other):
        # Overloading the '+' operator
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # Overloading the '-' operator
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )
complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, 2)

result_add = complex1 + complex2
print(f"Addition Result: {result_add}")
result_sub = complex1 - complex2
print(f"Subtraction Result: {result_sub}")
result_mul = complex1 * complex2
print(f"Multiplication Result: {result_mul}")
