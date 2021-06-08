st1 = input()
st2 = input()

temp = ''

for i in range(0,len(st1)):
  for j in range(0,len(st2)):
    if st1[i]==st2[j]:
      continue
    else:
      temp = temp +st2[j]
  st2 ,temp = temp, ""
print(st2)