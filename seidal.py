#seidal method
from math import *
a1=int(input("a1= "))
b1=int(input("b1= "))
c1=int(input("c1= "))
d1=int(input("d1= "))
a2=int(input("a2= "))
b2=int(input("b2= "))
c2=int(input("c2= "))
d2=int(input("d2= "))
a3=int(input("a3= "))
b3=int(input("b3= "))
c3=int(input("c3= "))
d3=int(input("d3= "))
if a1 > (b1+c1) :
    if b2 > (a2+c2) :
        if c3 > (a3+b3) :
            y=0
            z=0
            for l in range(0,10):
                for i in range(0,10):
                    x=(1/a1)*(d1-(b1*y)-(c1*z))
                    x=round(x,4)
                print(x)
                for j in range(0,10):
                    y=(1/b2)*(d2-(a2*x)-(c2*z))
                    y=round(y,4)
                print(y)
                for k in range(0,10):
                    z=(1/c3)*(d3-(a3*x)-(b3*y))
                    z=round(z,4)
                print(z)
                print("-------------")
                a=x
                b=y
                c=z
                if a==x:
                    break
                if b==y:
                    break
                if c==z:
                    break
                           