n = int(input())
i = 0

while i < n :
  j=0
  while j < n :
    if i==j or i+j==n-1 or j == n//2 or i == n//2 or i==0 or i==n-1 or j==0 or j ==n-1:
      print('*', sep='',end='')
    else:
      print(' ', sep='',end='')
    j=j+1
  i=i+1
  print()