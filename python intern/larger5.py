a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
d=int(input("Enter d value: "))
e=int(input("Enter e value: "))
if(a>b):
    if(a>c):
        if(a>d):
            if(a>e):
                print("A is Larger",a)
elif(b>c):
    if(b>d):
        if(b>e):
            print("B is Larger",b)
elif(c>d):
    if(c>e):
        print("C is Larger",c)
elif(d>e):
    print("D is Larger",d)
else:
    print("E is Larger",e)