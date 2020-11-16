number1 = int(input("Write number 1 "))
number2 = int(input("Write number 2 "))
count = 0
while number1>0 and number2>0:
  if number1%10 == number2%10:
    count = count + 1
  number1 = number1 // 10
  number2 = number2 // 10
  
print(count)



