total = 0
n = int(input())

if (n==0 and n==1):
  total = 0
if (n==2):
  total = 2
for i in range (2,n):
  for j in range(2,i):
    if (i%j == 0):
      break
  else:
    total = total + i
print(total)