import math
a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))
if (a<b) and (b<c):
    if c**2 == (a**2)+(b**2):
        print(1)
else:
    print(0)
        