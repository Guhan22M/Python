class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        pi=3.14
        return 2*pi*self.radius**2
    def perimeter(self):
        pi=3.14
        return 2*pi*self.radius
#main
radius = int(input("Enter the Radius: "))
obj1 = Circle(radius)
print("Perimeter of Circle is ",obj1.perimeter())