x=int(input("enter lower range: "))
s=int(input("enter upper range: "))
for i in range(x,s+1):
    z=0
    m=i
    while i>0:
        y=i%10
        z=z+(y*y*y)
        i=i//10
    if m==z:
        print(m)

