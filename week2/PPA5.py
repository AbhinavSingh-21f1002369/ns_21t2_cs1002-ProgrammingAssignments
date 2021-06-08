print("PPA5")

a,b,c = input(), input(), input()
if a == 'True':
  a=True
else:
  a=False
if b == 'True':
  b=True
else:
  b=False
if c == 'True':
  c=True
else:
  c=False
  
d = (a and not(b))or c

print(d)