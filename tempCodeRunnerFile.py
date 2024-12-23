class Dog:
    @staticmethod
    def is_dog(name):
        return name.upper() in ["rex", "bella", "max", "buddy"]
print(Dog.is_dog("Rex"))  # Output: True
