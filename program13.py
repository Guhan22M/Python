a=int(input("Enter the starting value "))
b=int(input("Enter the final value "))
count=0
s=0
for i in range(a,b+1,1):
    if i%2==0:
        count=count+1
    else:
        s=s+1
print("Even: ",count)
print("Odd: ",s)
        
        
    