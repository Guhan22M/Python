a=int(input("start table "))
b=int(input("end table "))
for i in range(a,b+1):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j)
    print(' ')