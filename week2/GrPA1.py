print("GrPA1")

a = int(input())
b = int(input())
c = int(input())

pair1 = (a**2) - (b**2) - (c**2)
pair2 = -(a**2) + (b**2) - (c**2)
pair3 = -(a**2) - (b**2) + (c**2)


if pair1==0 or pair2==0 or pair3==0:
  print("YES")
else:
  print("NO")