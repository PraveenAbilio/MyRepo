# class MyClass:
#     def __init__(self):
#         self._value = 10
    
#     @property
#     def get_value(self):
#         return self._value

#     @get_value.setter
#     def set_value(self, new_value):
#         self._value = new_value

# my_object = MyClass()

# initial_value = my_object.get_value
# print(f"Initial value: {initial_value}")

# my_object.set_value = 20

# updated_value = my_object.get_value
# print(f"Updated value: {updated_value}")


# table_of_five = [f"5 x {i} = {5 * i}" for i in range(1, 11)]

# with open('multiplication_table_5.txt', 'w') as file:
#     for line in table_of_five:
#         file.write(line + '\n')

# print("Multiplication table of 5 has been written to multiplication_table_5.txt.")


# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __mul__(self, other):
#         if isinstance(other, Vector2D):
#             result = self.x * other.x + self.y * other.y
#             return result
#         else:
#             raise TypeError("Multiplication not supported for non-Vector2D types")

# vector1 = Vector2D(2, 3)
# vector2 = Vector2D(4, 5)

# result = vector1 * vector2

# print(f"The dot product of {vector1} and {vector2} is: {result}")



