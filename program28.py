from math import *
def fact(n):
    sum=0
    for i in range(1,n+1):
        x=i/(factorial(i))
        sum=sum+x
    return sum
n=int(input("enter the number: "))
print(fact(n))
