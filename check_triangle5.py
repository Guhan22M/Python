a=int(input("Enter the first side length "))
b=int(input("Enter the second side length "))
c=int(input("enter the third side length "))
if ((b+c)>a) and ((a+c)>b) and ((a+b)>c):
    print("It is perfect triangle")
else:
    print("It is not a triangle")