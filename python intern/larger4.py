a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
d=int(input("Enter d value: "))
if(a>b):
    if(a>c):
        if(a>d):
            print("A is Larger",a)
elif(b>c):
    if(b>d):
        print("B is Larger",b)
elif(c>d):
    print("C is Larger",c)
else:
    print("D is Larger",d)