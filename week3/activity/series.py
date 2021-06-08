n = int(input())
num = "1"
total = 0
for i in range(1 , n + 1):
  total += int(num * i)
avg = total / n
print(avg)