a=int(input("Start Table "))
b=int(input("End Table"))
for i in range(a,b+1):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)
    print(' ')
