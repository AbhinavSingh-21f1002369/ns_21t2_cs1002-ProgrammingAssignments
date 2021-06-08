term = 1
count = 0
sum_series = 0
while term:
  sum_series = sum_series + (1 / term)
  count += 1
  term += 1
  if 10 - sum_series < 0.05:
    break
print("{:.2f}".format(sum_series))
print("{}".format(count))