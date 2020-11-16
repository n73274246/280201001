number_ofinteger = input("How many numbers are there? ")
count = 0
for i in number_ofinteger:
  n = int(input("Enter a number "))
  if n %2 == 0:
    count = count + 1
  number_ofinteger = int(number_ofinteger)
  percent = count/number_ofinteger * 100
print(percent)
