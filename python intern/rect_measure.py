class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
#main
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
obj1 = Rectangle(length,width)
print("Area of Rectangle is ",obj1.area())
print("Perimeter of Rectangle is ",obj1.perimeter())
