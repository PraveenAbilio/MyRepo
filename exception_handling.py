try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

else:
    print("Result:", result)

finally:
    print("This code always runs.")



 

