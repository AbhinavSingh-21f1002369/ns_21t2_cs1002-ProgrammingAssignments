n = int(input())
count = 1
for num in range(2,n+1):
  flag = True
  for j in range (2,num):
    if num % j == 0:
      flag = False
      break
  if flag == False:
    count += 1
print(count)