student_tot = int(input("Enter the number of students: "))
subject_tot = int(input("Enter the number of subjects: "))
print("")
all_stud_mark = []
naming = []
for i in range(1,student_tot+1):
    marks = []
    all_stud_mark.append(marks)
    name = input("Enter the name of the student: ")
    naming.append(name)
    for j in range(subject_tot): 
        sub = input(f"Enter the subject for {name}: ")
        mark = int(input(f"Enter the mark for {sub}: "))
        marks.append(mark)
    print("------------------")
print("Student name       Marks ")
for i,j in zip(naming,all_stud_mark):
    print(f"{i.upper()} <==>  {j}")