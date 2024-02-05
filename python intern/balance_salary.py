salary=[]
month=['JAN','FEB','MAR','APR','MAY','JUNE','JULY','AUG','SEPT','OCT','NOV','DEC']
salary_amt = int(input("Enter the salary: "))
for i in range(0,12):
    expense_amt = int(input(f"Enter the expense amount for {month[i]}: "))
    balance = salary_amt - expense_amt
    salary.append(balance)
    
print("Balance amount")
for x,y in zip(month,salary):
    print(f"{x} : {y}")
