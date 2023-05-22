b=1024
print("The Actual Price is ",b)
a=int(input("enter your age "))
if a>60:
    x=(a-(a*20/100))
    print("Your Discount will be added and the final price is ",x)
else:
    print("you are not under senior citizen category so your final price is ",b)