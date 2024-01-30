class Fibonacci:
    def __init__(self,number):
        self.number = number
    def fibo(self,number):
        if(number==0):
            return 0
        elif(number==1):
            return 1
        else:
            return self.fibo(number-1)+self.fibo(number-2)     
    def head(self):
          print("Fibonacci series")
    
number = 10
obj1 = Fibonacci(number)
obj1.head()
for i in range(0,number):
    print(obj1.fibo(i))