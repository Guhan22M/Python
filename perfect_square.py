n=int(input("enter the number "))
f=0
for i in range(1,n):
    if (i*i)==n:
        f=1
if f==1:
    print("it is perfect square ")
else:
    print("it is not perfect square ")