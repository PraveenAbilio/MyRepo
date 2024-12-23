# class MathOperations:
#     @staticmethod
#     def add(x, y):
#         return x + y

#     @staticmethod
#     def subtract(x, y):
#         return x - y

#     @staticmethod
#     def multiply(x, y):
#         return x * y

# def main():
#     result_add = MathOperations.add(5, 3)
#     result_subtract = MathOperations.subtract(8, 2)
#     result_multiply = MathOperations.multiply(4, 6)

#     print(f"Addition Result: {result_add}")
#     print(f"Subtraction Result: {result_subtract}")
#     print(f"Multiplication Result: {result_multiply}")
# if __name__ == "__main__":
#     main()


# # class Employee:
# #     def __init__(self,name,age,salary):
# #         assert age>=18, "age must be greater or equal to 18"
# #         self.name =name
# #         self.age=age
# #         self.salary=salary
# #     def printing_details (self):
# #         print(type(self.name))
# #         print(f"{self.name} of age {self.age} has salary of INR.{self.salary}")

# #         employee1=Employee("praveen",50000)
# #         employee1.printing_details()

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

def main():
    students_list = []

    student1 = Student("Praveen", 18, "A")
    students_list.append(student1)

    student2 = Student("Suresh", 19, "B")
    students_list.append(student2)

    student3 = Student("pavan", 20, "C")
    students_list.append(student3)

    print("Details of Students:")
    for student in students_list:
        print(student)
if __name__ == "__main__":
    main()


