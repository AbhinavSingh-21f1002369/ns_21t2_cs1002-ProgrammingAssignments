vowels = "aeiouAEIOU"

s = (input())

pos = 0

while pos<len(s) and s[pos] not in vowels:
  if s[pos].isalpha():
    print(s[pos],end=',')
  pos+=1