n = int(input())
prime = True
for i in range(2,n):
  if n % i == 0: #proves that it is a factor
    for j in range(2,i):
      if j%1 == 0:
        prime=False
    if prime :
      print(i)
  else:
    pass