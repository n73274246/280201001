year = int(input("Write a year "))
if year%4 == 0:
  if year%400== 0:
    print("It is a leap year.")
  else:
    print("Not a leap year")
else:
  print("Not a leap year")
