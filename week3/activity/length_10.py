s=input()
valid=False
for i in range(0,len(s)-4):
  count= s.count(s[i])
  if count > 4 :
    if s[i:i+5].count(s[i])==5:
      valid=True
  if valid==True:
    break
print(valid)