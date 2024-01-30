name1=input("Enter first name: ")
name2=input("Enter second name: ")
name3=input("Enter third name: ")
print("Alphabetical Order>>>")
if(name1<name2 and name1<name3):
    print(name1)
    if(name2<name3):
        print(name2)
        print(name3)
if(name2<name1 and name2<name3):
    print(name2)
    if(name1<name3):
        print(name1)
        print(name3)
if(name3<name1 and name3<name2):
    print(name3)
    if(name1<name2):
        print(name1)
        print(name2)
