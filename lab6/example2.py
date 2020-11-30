studentinfo = int(input("How many students? "))
examnotes = []
for i in studentinfo:
  midterm1 = int(input("Midterm 1: "))
  midterm2 = int(input("Midterm 2: "))
  final = int(input("Final: "))
  examnotes.append([midterm1,midterm2,final])
  average_grade = [midterm1*30/100 + midterm2*30/100 + final*40/100]
print(examnotes,average_grade)