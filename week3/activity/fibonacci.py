n = int(input("Enter any number: "))
a, b = 0, 1
print(a, b, end = ' ')
for i in range(3, n+1):
  fib = a + b
  print(fib, end = ' ')
  a = b
  b = fib