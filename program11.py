a=input("Enter your name ")
b=int(input("Enter your age "))
c=input("Enter your gender first letter in capital ")
d=int(input("Number of days worked "))
if c == 'M':
    if d>=18 and d<30:
        x=700
        print("your daily salary is ",x)
        y=d*x
        print("your salary according to your days worked ",y)
    else:
        print("you worked less than 18 days ")
if c== 'F':
    if d>=18 and d<30:
        i=750
        print("your daily salary is ",i)
        j=d*i
        print("your salary according to your days worked",j)
    else:
        print("you worked less than 18 days ")

