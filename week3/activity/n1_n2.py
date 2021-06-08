n1 = int(input())
n2 = int(input())
n1_count = 0
n2_count = 0
while n1>0:
  n1 = n1 // 10
  n1_count += 1
while n2>0:
  n2 = n2 //10
  n2_count += 1
if n1_count==n2_count:
  print("True")
else:
  print("False")