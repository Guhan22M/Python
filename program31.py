x=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    b=int(input("Enter the elements: "))
    x.append(b)
print(x)
for j in range(0,n):
    if x[j]%2==0:
        print("even value is ",x[j])
    else:
        print("odd value is ",x[j])