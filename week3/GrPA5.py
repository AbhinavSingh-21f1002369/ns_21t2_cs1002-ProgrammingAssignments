a=input()
flag='valid'
if(a[0] in '6789' and len(a)==10 and a.isnumeric()):
  for i in a:
    if(a.count(i)>7 or i*6 in a):
      flag = 'invalid'
      break
else:
  flag = 'invalid'
print(flag)