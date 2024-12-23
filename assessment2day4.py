# import random
# secret_number=random.randint(1,100)
# while True:
#     user_guess=int(input("guess the number(between 1 and 100)"))
#     if user_guess==secret_number:
#         print(f"congratulations you guessed the secret number:{secret_number}")
#         break
#     elif user_guess<secret_number:
#         print("your guess is high.try again")

#         print("your guess is low. try again.")


# for number in range(1, 21):
#     if number == 16:
#         continue
#     print(number)



# number = 5

# for i in range(10, 0, -1):
#     result = number * i
#     print(f"{number} x {i} = {result}")


# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __str__(self):
#         return f"{self.real} + {self.imag}j"

#     def __add__(self, other):
#         if isinstance(other, ComplexNumber):
#             result_real = self.real + other.real
#             result_imag = self.imag + other.imag
#             return ComplexNumber(result_real, result_imag)
#         else:
#             raise TypeError("Addition not supported for non-ComplexNumber types")

#     def __mul__(self, other):
#         if isinstance(other, ComplexNumber):
#             result_real = self.real * other.real - self.imag * other.imag
#             result_imag = self.real * other.imag + self.imag * other.real
#             return ComplexNumber(result_real, result_imag)
#         else:
#             raise TypeError("Multiplication not supported for non-ComplexNumber types")

# complex1 = ComplexNumber(2, 3)
# complex2 = ComplexNumber(4, 5)

# addition_result = complex1 + complex2

# multiplication_result = complex1 * complex2
# print(f"Complex Number 1: {complex1}")
# print(f"Complex Number 2: {complex2}")
# print(f"Addition Result: {addition_result}")
# print(f"Multiplication Result: {multiplication_result}")



# import random

# def guess_number():
#     secret_number = random.randint(1, 100)

#     print("Welcome to the Number Guessing Game!")
#     print("I have selected a number between 1 and 100. Can you guess it?")

#     attempts = 0

#     while True:
#         user_guess = input("Enter your guess: ")

#         try:
#             user_guess = int(user_guess)
#         except ValueError:
#             print("Please enter a valid number.")
#             continue
#         attempts += 1

#         if user_guess == secret_number:
#             print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
#             break
#         elif user_guess < secret_number:
#             print("Too low! Try again.")
#         else:
#             print("Too high! Try again.")

# if __name__ == "__main__":
#     guess_number()
