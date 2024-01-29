class Simpleinterset:
    def simple(self,p,n,r):
        self.p = p
        self.n = n
        self.r = r
        return self.p*self.n*self.r
    
p = int(input("Enter the principe amount: "))
n = int(input("Enter the number of years: "))
r =(int(input("Enter the rate of interest: ")))/100
obj1 = Simpleinterset()
print(f"Simple interest is {obj1.simple(p,n,r):.2f}")