#celsius to fahrenheit
print("celsius       fahrenheit")
space=' '
for c in range(0,100+1,10):
    f=(c*1.8)+32
    print(c,space*12,f)