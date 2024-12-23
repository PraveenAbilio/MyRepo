# num=float(input("enter a number:"))
# if num>0:
#     print ("positive")
# elif num==0:
#     print("zero")
# else:
#     print("negative")
string = "DATA SCIENCE"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
