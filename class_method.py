# class MyClass:
#     class_variable = "I am a class variable"

#     def __init__(self, instance_variable):
#         self.instance_variable = instance_variable
#     @classmethod
#     def show_class_variable(cls):
#         print(f"Class variable: {cls.class_variable}")

#     def show_instance_variable(self):
#         print(f"Instance variable: {self.instance_variable}")

# def main():
#     obj = MyClass(instance_variable="I am an instance variable")
#     obj.show_instance_variable()

#     MyClass.show_class_variable()

# if __name__ == "__main__":
#     main()


class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

def main():
    student = Student(name="John", age=20)
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    student.name = "Praveen"
    student.age = 25
    print(f"Updated Name: {student.name}")
    print(f"Updated Age: {student.age}")

if __name__ == "__main__":
    main()
