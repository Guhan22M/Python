class Slope:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
    def measure(self):
        return (y-c)/x
    
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
c = int(input("Enter the value of c: "))
obj1 = Slope(x,y,c)
print("Slope value (m) is ",obj1.measure())