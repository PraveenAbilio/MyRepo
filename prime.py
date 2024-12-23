# num = 29
# flag = False
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")


# num = 11
# if num > 1:
# 	for i in range(2, int(num/2)+1):
# 		if (num % i) == 0:
# 			print(num, "is not a prime number")
# 			break
# 	else:
# 		print(num, "is a prime number")
# else:
# 	print(num, "is not a prime number")




# Program to check if a number is prime or not

# num = 21

# # To take input from the user
# #num = int(input("Enter a number: "))

# # define a flag variable
# flag = False

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")

# num = 407

# # To take input from the user
# #num = int(input("Enter a number: "))

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
       
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")
        


 
# # Input from the user
# num = int(input("Enter a number: "))

# # If number is greater than 1
# if num > 1:
#    # Check if factor exist  
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")
       
# # Else if the input number is less than or equal to 1
# else:
#    print(num,"is not a prime number")



#    # Program to check if a number is prime or not

# Input from the user
# num = int(input('Please enter a number:'))
# # Declaring and Initialization of two integer type variable
# i = 2
# flag = 0
# while i<num:
#     if num%i == 0:
#         #If Yes,update flag value
#         flag = 1
#         print (num,"is NOT a prime number");
#     #Updating the value of i on every iteration by 1
#     i = i + 1
# #checking the value of flag
# if flag == 0:
#     #If Yes, Then it is a prime number
#    print (num,"is a prime number!")
