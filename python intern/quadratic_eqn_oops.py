import math
class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def root1(self):
        x=math.sqrt((b**2)-(4*a*c))
        return (-b+x)/(2*a)
    
    def root2(self):
        x=math.sqrt((b**2)-(4*a*c))
        return (-b-x)/(2*a)
    
a = int(input("Enter the A value: "))
b = int(input("Enter the B value: "))
c = int(input("Enter the C value: "))
obj1 = Quadratic(a,b,c)
print("Roots are",obj1.root1(),"and",obj1.root2())