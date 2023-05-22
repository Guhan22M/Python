a=int(input("enter the wind speed "))
b=int(input("enter the temperature "))
c=13.12+0.6215*b-11.37*a**0.16+0.3965*a*b**0.16
print("the wind chill index is ",c)