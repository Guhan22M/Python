class CompoundInterest:
    def compund(self,p,n,r,t):
        self.p = p
        self.n = n
        self.r = r
        self.t = t
        a=p*((1+(r/n))**(n*t))
        return a-p
       
p = int(input("Enter the principle amount: "))
n = int(input("Enter the number of times interest is compound: "))
r = (int(input("Enter the rate of interest: ")))/100
t = int(input("Enter the time: "))
obj1 = CompoundInterest()
print("Compund Interest is ",obj1.compund(p,n,r,t))