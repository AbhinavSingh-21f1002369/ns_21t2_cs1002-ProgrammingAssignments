num_of_terms = int(input())
term = 1
count = 0
sum_series = 0
for term in range(1, num_of_terms + 1):
  sum_series = sum_series + 1 / term
  count += 1
  term += 1
print("{:.2f}".format(count / sum_series))