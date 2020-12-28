def f(n):
  if n == 0:
    return 0
  return 3+f(n-1)

print(f(3))