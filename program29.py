def series(x,n):
    g=0
    for i in range(2,n+1):
        a=1
        g=g+(x/a*2)
    return g
x=int(input("Enter the value of x: "))
n=int(input("Enter the number of times iterated: "))
print(series(x,n))
