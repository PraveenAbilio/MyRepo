v1 = "2DVector(length=3)"
v2 = "2DVector(length=4)"
v3 = "3DVector(length=5)"
v4 = "3DVector(length=6)"


print(v1.length)
print(v1.direction) 
print(v1.position) 

print(v2.length) 
print(v2.direction) 
print(v2.position) 

print(v3.position) 
print(v4.position) 




class Animal:
    def _init_(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"


class Pet(Animal):
    def play(self):
        return f"{self.name} is playing"


class Dog(Pet):
    def bark(self):
        return "Woof! Woof!"
animal = Animal("Generic Animal")
pet = Pet("Fluffy")
dog = Dog("Buddy")


print(animal.eat())  
print(pet.eat())     
print(pet.play())   

print(dog.eat())     
print(dog.play())    
print(dog.bark())    



class Employee:
    def _init_(self, name, salary, increment):
        self.name = name
        self._salary = salary
        self._increment = increment  

    @property
    def salary(self):
        return self._salary

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        if value >= 0:
            self._increment = value
        else:
            print("Increment must be a non-negative value.")

    def salary_after_increment(self):
        new_salary = self.salary + self.increment
        return f"{self.name}'s new salary after increment: {new_salary}"
employee = Employee("John Doe", 50000, 2000)
print(f"{employee.name}'s current salary: {employee.salary}")
print(f"{employee.name}'s current increment: {employee.increment}")
employee.increment = 2500
print(f"{employee.name}'s updated increment: {employee.increment}")
print(employee.salary_after_increment())


class Complex:
    def _init_(self, real, imag):
        self.real = real
        self.imag = imag

    def _str_(self):
        return f"{self.real} + {self.imag}j"

    def _add_(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return Complex(real_sum, imag_sum)

    def _mul_(self, other):
        real_product = (self.real * other.real) - (self.imag * other.imag)
        imag_product = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_product, imag_product)
complex1 = Complex(2, 3)
complex2 = Complex(1, 4)
result_addition = complex1 + complex2
result_multiplication = complex1 * complex2
print("Complex 1:", complex1)
print("Complex 2:", complex2)
print("Addition:", result_addition)
print("Multiplication:", result_multiplication)



class Vector:
    def _init_(self, components):
        self.components = components

    def _str_(self):
        return f"Vector({self.components})"

    def _add_(self, other):
        if len(self.components) == len(other.components):
            sum_components = [a + b for a, b in zip(self.components, other.components)]
            return Vector(sum_components)
        else:
            raise ValueError("Vectors must have the same dimensions for addition.")

    def _mul_(self, other):
        if len(self.components) == len(other.components):
            dot_product = sum(a * b for a, b in zip(self.components, other.components))
            return dot_product
        else:
            raise ValueError("Vectors must have the same dimensions for dot product.")
vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])
result_sum = vector1 + vector2
result_dot_product = vector1 * vector2
print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Sum:", result_sum)
print("Dot Product:", result_dot_product)


