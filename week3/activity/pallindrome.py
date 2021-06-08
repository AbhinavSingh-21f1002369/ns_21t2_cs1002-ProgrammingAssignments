
st = input()
reverse = ""
for char in st:
  reverse = char + reverse

if reverse == st:
  print("Pallindrome")
else :
  print("Not Pallindrome")