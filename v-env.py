# def main():
#     name = input("Enter the name of the student: ")
#     marks = int(input("Enter the marks of the student: "))
#     phone_number = input("Enter the phone number of the student: ")

#     formatted_string = "The name of the student is {}, his marks are {} and the phone number is {}".format(name, marks, phone_number)
#     print(formatted_string)

# if __name__ == "__main__":
#     main()

# def convert_to_vertical_string(table):
#     vertical_string = "\n".join(str(number) for number in table)
#     return vertical_string

# def main():
#     multiplication_table_of_7 = [7 * i for i in range(1, 11)]

#     vertical_string = convert_to_vertical_string(multiplication_table_of_7)

#     print("Multiplication Table of 7:")
#     print(vertical_string)

# if __name__ == "__main__":
#     main()

# def filter_by_divisible_5(numbers):
#     divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))
#     return divisible_by_5

# def main():

#     numbers = [10, 25, 7, 30, 15, 42, 50, 3, 20]

#     divisible_by_5 = filter_by_divisible_5(numbers)

#     print("Original list:", numbers)
#     print("Numbers divisible by 5:", divisible_by_5)

# if __name__ == "__main__":
#     main()

# from functools import reduce

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     maximum = reduce(lambda x, y: x if x > y else y, numbers)
#     return maximum

# def main():
#     numbers = [10, 25, 7, 30, 15, 42, 50, 3, 20]

#     max_number = find_maximum(numbers)

#     if max_number is not None:
#         print("Original list:", numbers)
#         print("Maximum number:", max_number)
#     else:
#         print("The list is empty.")

# if __name__ == "__main__":
#     main()



