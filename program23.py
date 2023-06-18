#program of simple interestg
def simple_interest(a):
    if b>=60:
        r=12
        si=p*n*r
        print("your simple interest is ",si)
    elif c=='F' or c=='f':
        r=10
        si=p*n*r
        print("your simple interest is ",si)
    else:
        r=9
        si=p*n*r
        print("your simple interest is ",si)
        
a=input("Enter your name: ")
b=int(input("Enter your age: "))
c=input("Enter the gender first letter: ")
p=int(input("Enter the principle amount: "))
n=int(input("Enter number of years: "))
simple_interest(a)
