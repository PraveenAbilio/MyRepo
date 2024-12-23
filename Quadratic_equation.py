# import cmath
# a,b,c= 1,-6,13

# determinant = cmath.sqrt(b**2 - 4*a*c)
# x1 = (-b + determinant) / (2*a)
# x2 = (-b - determinant) / (2*a)
# print(x1,x2)


# num=2345,6789
# sum=0
# while(num>0):
#     sum=sum+num%10
#     num=num//10
#     print(sum)



def recursivemethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursivemethod(n-1)
    print(n)





