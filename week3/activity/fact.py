'''n = int(input())
total = 0
for i in range(1,n+1):
  fact = 1
  j = 1
  while j <= i:
    fact *= j
    j += 1
  total += fact
avg = total / n
print(avg)

'''
n = int(input())
i = 1
total = 0
while i <= n:
  fact = 1
  for j in range(1,i+1):
    fact *= j
  total += fact
  i += 1
avg = total / n
print(avg)
#'''