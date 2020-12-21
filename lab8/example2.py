def is_prime(x):
  x = int(x)
  if x > 2:
    for i in range(2,x):
      if x%i != 0:
        return x
  else:
    return False
def print_primes_between(x,y):
  for i in range(x,y):
    
    if is_prime(i):
      print(i, end=" ")
def main():
  x = int(input("Begin: "))
  y = int(input("End: "))
  print_primes_between(x,y)

main()







