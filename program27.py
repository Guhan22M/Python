a=input("Enter the first string: ")
b=input("Enter the second string: ")
x=list(a)
y=list(b)
for i in y:
    if i in x:
        x.remove(i)
if len(x) == 0:
    print("no")
else:
    print("yes")