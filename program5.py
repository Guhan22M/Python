a=int(input("enter the length of 1st "))
b=int(input("enter the length of 2nd "))
c=int(input("enter the length of 3rd "))
if (a+b)>c and (b+c)>a and (a+c)>b:
    print("it is triangle ")
else:
    print("it is not a trinagle")