name = input("Write name ")
salary = input("Write salary ")
employees = {name: salary}
count = 0
for employee in employees: 
 name = input("Write name ")
 salary = input("Write salary ")
 count = count + 1
 if count == 5:
   break



print(employees)