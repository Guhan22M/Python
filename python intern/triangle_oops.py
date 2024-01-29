class Triangle:
    def perimeter(self,base,side1,side2):
        self.base = base
        self.side1 = side1
        self.side2 = side2
        return self.base+self.side1+self.side2
    
    def area(self,base,height):
        self.base = base
        self.height = height
        return self.base*self.height
#main
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
side1 = int(input("Enter the side1: "))
side2 = int(input("Enter the side2: "))
obj1 = Triangle()
print("Perimeter of Triangle ",obj1.perimeter(base,side1,side2))
print("Area of Triangle ",obj1.area(base,height))