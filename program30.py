def series(n):
    sum=0
    for i in range(15,(n*15)+1,15):
        sum=sum+i
        if i==(n*15):
            break
    return sum
n=int(input("entr the number of elements: "))
print(series(n))