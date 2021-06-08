n=int(input())
for i in range(0,n):
  print(" "*2*i,end="")
  for j in range(n-i,1,-1):
    print(j,end=" ")
  for k in range(1,n-i+1):
    if k == n-i:
      print(k,end="")
    else:
      print(k,end=" ")
  print(" "*2*i,end="")
  print()