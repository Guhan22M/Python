class Square:
    def __init__(self,value):
        self.value = value
        
    def area(self):
        return self.value*self.value
    def perimeter(self):
        return 4*self.value
    
#main
side = int(input("Enter the side length: "))
obj1 = Square(side)
print("Area of square is ",obj1.area())
print("Perimeter of Square is ",obj1.perimeter())
