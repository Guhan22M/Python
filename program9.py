print("Welcome to Rotaract Club ")
x=int(input("Enter your age "))
y=int(input("Enter your weight "))
if x>18:
    if y>40:
        print("You are eligible to donate blood ")
        name=input("Enter your name ")
        print("your age is ",x)
        print("your weight is ",y)
        print(1)
else:
    print(0)