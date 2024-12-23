
# 1.Write a program to calculate area of a circle.

import math  
  
def calculate_area (Radius):   
        return math.pi * Radius ** 2
Radius = float (input ("Please enter the radius of the given circle: "))  
print (" The area of the given circle is: ", calculate_area (Radius))  


# 2.Write a program to calculate simple interest.

p=100
r=1
t=2
simple_interest = (p+r+t)/100
print("the simple interest is:", simple_interest)


# 3.Write a program to check whether input alphabet is vowel or not.

character = input("Enter a character: ")  
  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
if character in vowels:  
    print(f"The character '{character}' is a vowel!")  
else:  
    print(f"The character '{character}' is a consonant!")  

def isVowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if char in vowels:  
     print(f"The character'{char}' is a vowel!")  
    else:  
     print(f"The character '{char}' is a consonant!") 
character= input("Enter a character: ")
isVowel(character)
 

# 4.Write a program to input two integer numbers and display the sum of even numbers between these two input numbers.


def sum_of_even_numbers(start, end):
    if start > end:
        start, end = end, start
    total_sum = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            total_sum += num

    return total_sum

start_num = int(input("Enter the first integer: "))
end_num = int(input("Enter the second integer: "))

result = sum_of_even_numbers(start_num, end_num)
print(f"The sum of even numbers between {start_num} and {end_num} is: {result}")


# 5.Write a program to read a sentence and count the number of characters and words in that sentence.


string=input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)


# 6.Write a Program to Find the Frequency of Characters in a String.

a=input()
b=[]
for i in a:
 if(i not in b):
  print(i,":",a.count(i))    #vertical
b.append(i)


string = "Yolo Life"

for i in string:
    frequency = string.count(i)                      #horizontal
    print(str(i) + ": " + str(frequency), end=", ")



# str = "YOLO LIFE"

# dict = {}

# for i in str:
#     if i in dict:
#         dict[i] += 1

#     else:
#         dict[i] = 1

# print(dict)



string = "praveenkumarrrrr"
res = {i: string.count(i) for i in set(string)}

print(res)


# 7.Write a python program to calculate simple interest and amount from principal, time and rate using class, objects and functions.


class SimpleInterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_simple_interest(self):
        interest = (self.principal * self.rate * self.time) / 100
        return interest

    def calculate_total_amount(self):
        interest = self.calculate_simple_interest()
        total_amount = self.principal + interest
        return total_amount

# Take user input for principal amount, rate of interest, and time (in years)
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the time period in years: "))

# Check if the principal amount and time are non-negative
if principal < 0 or time < 0:
    print("Please enter non-negative values for principal amount and time.")
else:
    # Create an object of SimpleInterestCalculator class
    interest_calculator = SimpleInterestCalculator(principal, rate, time)

    # Calculate simple interest and total amount using class methods
    interest = interest_calculator.calculate_simple_interest()
    total_amount = interest_calculator.calculate_total_amount()

    # Display the results
    print(f"Principal Amount: {principal}")
    print(f"Rate of Interest: {rate}%")
    print(f"Time Period: {time} years")
    print(f"Simple Interest: {interest:.2f}")
    print(f"Total Amount: {total_amount:.2f}")

