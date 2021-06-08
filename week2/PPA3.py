print("PPA3")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())


if y2-y1==0:
  print("Horizontal Line")
elif x2-x1==0 :
  print("Vertical Line")
else :
  m = (y2 - y1) / (x2 - x1)
  y3 = (m * (x3 - x1))+ y1
  if m>0:
    print(y3)
    print("Positive Slope")
  else:
    print(y3)
    print("Negative Slope")