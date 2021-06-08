st = input()
prod = 1
for char in st:
  if char == '-':
    continue
  else:
    prod = prod * int(char)

print(prod)