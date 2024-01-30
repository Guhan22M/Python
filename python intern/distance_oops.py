import math
class Distance:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def measure(self):
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    
x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))
x2 = int(input("Enter the value of x2: "))
y2 = int(input("Enter the value of y2: "))
obj1 = Distance(x1,y1,x2,y2)
print("Distance between the two points are",obj1.measure())