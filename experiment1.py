#logical programs
x=int(input("enter the  number "))
if x%2!=0:
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    print("the factorial of ",x,"is ",fact)
    y=0
    while fact>0:
        y=y+1
        fact=fact//10
    print("the number of digits is ",y)
else:
    sum=0
    k=x
    while x>0:
        z=x%10
        sum=sum*10+z
        x=x//10
    if k == sum:
        print("it is palindrome ")