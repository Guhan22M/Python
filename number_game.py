import random
a=random.randint(1,20)
y=int(input("enter the number "))
while y!=a:
    if y>a:
        print("the number is greater than random number")
    else:
        print("thr number is smaller than random number ")
    print("enter number again ")
    y=int(input("enter the number"))
print("you found it ")