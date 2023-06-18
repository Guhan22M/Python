# perfect square or not
import math
def square(x):
    y=math.sqrt(x)
    if math.ceil(y) == math.floor(y):
        print("it is perfect square ")
    else:
        print("it is not perfect square")    
a=int(input("enter the number "))
square(a)