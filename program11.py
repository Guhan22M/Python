a=1
b=2
c=3
d=4
e=5
print("Welcome to our Restaurant ")
n=1200
print("Your bill amount is ",n)
print("please fill our Restaurant food rating")
x=int(input("Enter Food rating from 1 to 5: "))
y=int(input("Enter service rating from 1 to 5: "))
z=int(input("Enter ambience rating from 1 to 5: "))
if x==4 or x==5:
   if (y==4 or y==5) and (z==4 or z==5) :
       i=(n*10)/100
       print("Your tips is ",i)
   else:
       i=(n*5)/100
       print("Your tip is ",i)
elif x==3 or x==2 or x==1:
    if (y==4 or y==5) and (z==4 or z==5):
        j=(n*5)/100
        print("Your tip is ",j)
    else:
        j=(n*1)/100
        print("Your tip is ",j)
        
    