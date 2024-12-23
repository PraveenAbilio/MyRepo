# # def open_files(file_names):
# #     for file_name in file_names:
# #         try:
# #             with open(file_name, 'r') as file:
# #                 print(f"File '{file_name}' opened successfully.")
# #         except FileNotFoundError:
# #             print(f"File '{file_name}' not found. Please check the file path.")

# # def main():
# #     file_names = ['1.txt', '2.txt', '3.txt']
# #     open_files(file_names)

# # if __name__ == "__main__":
# #     main()


# # def print_specific_elements(input_list):
# #     for index, value in enumerate(input_list):
# #         if index in {2, 4, 6}:
# #             print(f"Element at index {index}: {value}")

# # def main():
# #     my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# #     print_specific_elements(my_list)

# # if __name__ == "__main__":
# #     main()


# # def generate_multiplication_table(number):
# #     table = [number * i for i in range(1, 11)]
# #     return table

# # def main():
# #     user_number = int(input("Enter a number: "))

# #     multiplication_table = generate_multiplication_table(user_number)
# #     print(f"Multiplication Table for {user_number}: {multiplication_table}")

# # if __name__ == "__main__":
# #     main()


# # def display_fraction(a, b):
# #     try:
# #         result = a / b
# #         print(f"The result of {a}/{b} is: {result}")
# #     except ZeroDivisionError:
# #         print("Cannot divide by zero. Result is infinite.")

# # def main():
# #     a = int(input("Enter an integer for 'a': "))
# #     b = int(input("Enter an integer for 'b': "))

# #     display_fraction(a, b)

# # if __name__ == "__main__":
# #     main()


# # def generate_and_write_tables(file_path):
# #     with open(file_path, 'w') as file:
# #         for i in range(2, 21):
# #             table_content = f"Multiplication Table for {i}:\n"
# #             for j in range(1, 11):
# #                 result = i * j
# #                 table_content += f"{i} x {j} = {result}\n"
# #             table_content += "\n"

# #             file.write(table_content)

# # def main():
# #     file_path = "tables.txt"
# #     generate_and_write_tables(file_path)

# #     print(f"Multiplication tables have been generated and saved in the '{file_path}' file.")

# # if __name__ == "__main__":
# #     main()


