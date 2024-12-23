# import math
# def calculate_area(Radius):
#     return math.pi * Radius ** 2
# Radius=float(input("enter the number of radius of circle:",))
# print("the radius of given circle is :", calculate_area(Radius))


# p=200
# r=1
# t=2
# simple_interest=(p+r+t)/100
# print("the simple interest is:", simple_interest)


# character=input("enter a character:")
# vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# if character in vowels:
#     print(f" the character {character} is a vowel")
# else:
#     print(f" the character {character} is a consonant")


# def sum_of_even_numbers(start,end):
#     if start > end:
#       start, end=end,start
#     total_sum=0
#     for num in range(start,end+1):
#       if num%2==0:
#         total_sum+=num
#     return total_sum
# start_num=int(input("enter the starting number:"))
# end_num=int(input("enter the ending number:"))
# result=sum_of_even_numbers(start_num,end_num)
# print(f"the sum of even numbers between {start_num} and {end_num}: {result}")
                

# def sum_of_even_numbers(start, end):
#     if start > end:
#         start, end = end, start
#     total_sum = 0

#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             total_sum += num

#     return total_sum

# start_num = int(input("Enter the first integer: "))
# end_num = int(input("Enter the second integer: "))

# result = sum_of_even_numbers(start_num, end_num)
# print(f"The sum of even numbers between {start_num} and {end_num} is: {result}")


# string=input("enter string:")
# char=0
# word=1
# for i in string:
#     char=char+1
#     if(i==' '):
#         word=word+1
# print("number of words in string:")
# print(word)
# print("number of characters in string:")
# print(char)

# string=" praveen kumar"
# for i in string:
#     frequency=string.count(i)
#     print(str(i) + ":" + str (frequency), end= ", ") 

# a= input()
# b=[]
# for i in  a:
#     if (i  not in b):
#      print(i,":",a.count(i))
# b.append(i)


# def fahrenheit_to_celsius(fahrenheit):
#     celsius=celsius(5*(fahrenheit-32))/9
#     return celsius

# fahrenheit_temperature=float(input("enter temperature in fahrenheit "))

# celsius_temperature= fahrenheit_to_celsius(fahrenheit_temperature)

# print(f"{fahrenheit_temperature} degrees fahrnheit is equal to {celsius_temperature:.2f} degree celsius.")

    
# def count_words_with_suffix(sentence, suffix):
#     words=sentence.split()
#     count=0

#     for word in words:
#         if word.endswith(suffix):
#             count+=1

#     return count

# input_string = "there is a mango in the tree where a monkey is hanging."

# suffix_to_count='e'
# result=count_words_with_suffix(input_string,suffix_to_count)
# print(f" the number of words ending with' {suffix_to_count}' is: {result}")



import re
text1 ='CJM'
print("original string:",text1)
print("without extra spaces:", re.sub(' +', ' ',text1))
