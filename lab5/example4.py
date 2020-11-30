password = "abc123"
user = input("Write password")
while password != user:
  print("Wrong")
  print(user)
  if user == ("Help"):
    print(password[0])
while password == user:
  print("Welcome")