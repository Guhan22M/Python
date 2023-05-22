a=int(input("Enter your salary "))
b=int(input("Enter your experience "))
if b>10:
    x=(a*(10/100))+a
    print("your salary with bonus ",x)
elif (b>6 and b<10):
    y=(a*(8/100))+a
    print("your salary with bonus ",y)
else:
    z=(a*(5/100))+a
    print("your salary with bonus ",z)
