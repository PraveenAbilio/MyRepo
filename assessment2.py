# import random
# random_numbers = [random.randint(1, 100) for _ in range(10)]

# print("Unsorted List:", random_numbers)

# random_numbers.sort()

# print("Sorted List:", random_numbers)


# class Bank_Account:
#     def __init__(self):
#         self.balance=0
#         print("Welcome to Deposit & Withdrawal Machine!")
        
#     def deposit(self):
#         amount=float(input("Enter amount to be deposited: "))
#         self.balance += amount
#         print("Amount Deposited: ",amount)
#     def withdraw(self):
#         amount = float(input("Enter amount to withdraw: "))
#         if self.balance>=amount:
#             self.balance-=amount
#             print("You withdraw: ",amount)
#         else:
#             print("Insufficient balance ")
#     def display(self):
#         print("Net Available Balance=",self.balance)
# s = Bank_Account()
# s.deposit()
# s.withdraw()
# s.display()

# fname = input("Enter file name: ")
 
# num_words = 0
 
# with open(fname, 'r') as f:
#     for line in f:
#         words = line.split()
#         num_words += len(words)
# print("Number of words:")
# print(num_words)

# global_variable = "I am a global variable"

# def example_function():
#     local_variable = "I am a local variable"
    
#     print("Inside the function:", global_variable)

#     print("Inside the function:", local_variable)

# print("Outside the function:", global_variable)

# example_function()



# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
        
#     def display(self):
#         print ("Length of Rectangle is: ", self.length)
#         print ("Breadth of Rectangle is: ", self.breadth)
        
#     def area(self):
#         return (self.length*self.breadth)
    
#     def perimeter(self):
#         return (2*self.length + 2*self.breadth)
    
# l = int (input("Enter the length of the Rectangle: "))
# b = int (input("Enter the breadth of rectangle: "))

# r1 = Rectangle(l , b)
# print ("Rectangle object details are:")
# r1.display()
# print("")
# print ("Area of Rectangle is: ", r1.area())
# print("")
# print ("The Perimeter of the Rectangle is: ", r1.perimeter())

# list_of_nums = [1, 2, 3, 12, 30, 15, 8]

# filtered_nums = filter(lambda x: x > 10, list_of_nums)

# sum_of_filtered_nums = sum(filtered_nums)

# print(f"List of numbers: {list_of_nums}")
# print(f"Filtered numbers (greater than 10): {list(filtered_nums)}")
# print(f"Sum of filtered numbers: {sum_of_filtered_nums}")


# student_scores = {
#     "praveen": 85,
#     "naveen": 92,
#     "suresh": 78,
#     "pavan": 95,
#     "harish": 88
# }
# print("Original student scores:")
# for name, score in student_scores.items():
#     print(f"{name}: {score}")

# sorted_scores = sorted(student_scores.items(), key=lambda x: x[1])

# print("\nSorted student scores:")
# for name, score in sorted_scores:
#     print(f"{name}: {score}")


# def is_prime(number):
#     if number <= 1:
#         return False
#     elif number == 2:
#         return True
#     elif number % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(number**0.5) + 1, 2):
#             if number % i == 0:
#                 return False
#         return True

# def main():
#     user_number = int(input("Enter a number: "))

#     if is_prime(user_number):
#         print(f"{user_number} is a prime number.")
#     else:
#         print(f"{user_number} is not a prime number.")

# if __name__ == "__main__":
#     main()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)


# p1 = Point(1, 2)
# p2 = Point(2, 3)

# print(p1+p2)


# def is_prime(number):
#     if number <= 1:
#         return False
#     elif number == 2:
#         return True
#     elif number % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(number**0.5) + 1, 2):
#             if number % i == 0:
#                 return False
#         return True

# def print_primes_in_range(start, end):
#     print(f"Prime numbers between {start} and {end}:")
#     for num in range(start, end + 1):
#         if is_prime(num):
#             print(num, end=" ")

# print_primes_in_range(1, 100)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    
    def calculate_area(self):
       area=self.length* self.width
       print ("the area of Rectangle is ",area)
    
    def calculate_perimeter(self):
        perimeter= 2*(self.length + 2*self.width)
        print ("the perimeter of Rectangle is ",perimeter)

    

rect = Rectangle(5,8)
rect.calculate_area()
rect.calculate_perimeter()




