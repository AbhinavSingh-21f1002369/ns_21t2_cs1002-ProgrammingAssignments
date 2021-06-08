st = input()

def isprime(n):
  Flag = True
  for i in range(2,n):
    if n%i == 0:
      Flag = False
  return Flag

for i in range(2,len(st)):
  if isprime(i):
    print(st[i])