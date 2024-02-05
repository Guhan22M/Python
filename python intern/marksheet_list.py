name = input("Enter your Name: ")
n = int(input("Enter Total number of subjects: "))
sum=0
det = []
for i in range(1,n+1):
    subject=input((f"Enter subject {i}: "))
    mark = int(input(f"Enter mark of {subject}: "))
    print("---")
    det.append(f"{subject} ==> {mark}")
    sum=sum+mark
total = sum
avg = total/n
print("-----MARK SHEET-----")
print("Student Name: ",name.upper())
print("Number of Subjects: ",n)
print("Marks based on subjects...")
for i in det:
    print(i)
print("Total Mark is ",total)
print(f"Average Mark is {avg:.2f}")