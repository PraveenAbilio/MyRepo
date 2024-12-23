# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Square(Shape):

#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def perimeter(self):
#         return 4 * self.side
# square_instance = Square(side=5)

# print("Area:", square_instance.area())
# print("Perimeter:", square_instance.perimeter())


class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        return f"{self.name} is barking"
    
my_dog=dog("rex",3)
print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())  




        