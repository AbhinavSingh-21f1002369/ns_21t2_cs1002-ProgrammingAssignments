st = input()

st = st.lower()

letters = "abcdefghijklmnopqrstuvwxyz"
out = ""
count = 0
for letter in letters :
  count = st.count(letter)
  out = out + letter*count

print(out)