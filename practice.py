# for i in range (1,20):
#     if i%2==0:
#         print(i,end=",")

# num=int(input("enter the number:"))
# for i in range(0,num+1):
#     if i%2==0:
#         print(i,end=",")

        

# i=0
# while i<=0:
#    if i%2==0:
#        print(i,end=",")
#        i+=


# num=12
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)
 
# i=1
# while i <=10:
#     print(i)
#     i+=1




# Python program to check whether
# the number is positive, negative
# or equal to zero

def check(n):
	
	# if the number is positive
	if n > 0:
		print("Positive")
		
	# if the number is negative
	elif n < 0:
		print("Negative")
		
	# if the number is equal to
	# zero
	else:
		print("Equal to zero")
		
# Driver Code
check(5)
check(0)
check(-5)
