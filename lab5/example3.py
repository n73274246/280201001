number1 = list(input("Write number 1"))
number2 = list(input("Write number 2"))
count = 0
number_1 = sorted(number1, reverse=True)
number_2 = sorted(number2, reverse= True)
for i in range(2):
  if number_1[:] == number_2[:]:
    count = count +1
print(count)

