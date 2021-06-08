name = input()

for i in range(0,len(name)):
  if i==0:
    print(name[0].upper(),end='')
  elif name[i].isspace():
    print(name[i+1].upper())
  else :
    pass