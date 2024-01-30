class Square:
    def __init__(self,number):
        self.number = number
    def squaring(self,number):
        for i in range(1,number+1):
                print(i*i)
    def head(self):
        print("Square of a number ")
number = 5
obj1 = Square(number)
obj1.head()
obj1.squaring(number)