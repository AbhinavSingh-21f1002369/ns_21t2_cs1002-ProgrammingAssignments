a,b,c,d,e = int(input()), int(input()), int(input()), int(input()), int(input())

def evensum(x,y):
  sum = x+y
  if sum%2 == 0:
    return(True)
  else:
    return(False)

if evensum(a,b) and evensum(b,c) and evensum(c,d) and evensum(d,e) and evensum(a,e):
  print("YES")
else:
  print("NO")