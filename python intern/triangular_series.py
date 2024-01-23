class Triangle:
    def __init__(self,number):
        self.number = number
    def series(self,number):
        self.number = number
        sum=0
        for i in range(1,number+1):
            sum=sum+i
            print(sum)
    def head(self):
        print("Triangular series")
            
number = 10
obj1 = Triangle(number)
obj1.head()
obj1.series(number)
