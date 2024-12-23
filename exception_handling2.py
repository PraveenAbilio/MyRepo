# def divide_numbers():
#     try:
#         num1 = int(input("Enter a numerator: "))
#         num2 = int(input("Enter a denominator: "))
#         result = num1 / num2

#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")

#     except ValueError:
#         print("Error: Please enter valid integers.")

#     else:
#         print("Result:", result)

#     finally:
#         print("This code always runs.")
# divide_numbers()


# def greet_user():
#     try:
#         name = input("Enter your name: ")
#         print("Hello, " + name + "! Nice to meet you.")

#     except KeyboardInterrupt:
#         print("\nProgram terminated by user.")

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     finally:
#         print("Thank you for using the program.")
# greet_user()


# def calculate_square_root(number):
#     if number < 0:
#         raise ValueError("Cannot calculate square root of a negative number.")
    
#     return number ** 0.5

# def main():
#     try:
#         user_input = float(input("Enter a non-negative number: "))

#         result = calculate_square_root(user_input)
#         print(f"The square root of {user_input} is: {result}")

#     except ValueError as ve:
#         print(f"Error: {ve}")

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()


def divide_numbers():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = numerator / denominator

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter valid integers.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        print(f"Result: {result}")

    finally:
        print("Thank you for using the program.")
divide_numbers()
