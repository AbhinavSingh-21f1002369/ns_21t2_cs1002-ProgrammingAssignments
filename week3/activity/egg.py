'''
box = input()
total_box = 0
egg = 0
for char in box:
  if char == '0':
    egg = egg + 1
  if char == "|":
    total_box = total_box + 1
total_box = total_box - 1
print("The total number of box =",total_box)
print("The total number of empty box =",total_box - egg)
print("Tumber of boxes that have eggs in them =",egg)

'''
#|0||0|||0|
#|0||0|||0|
#0|
#||
#0|


box = str(input())
egg_box= 0
emp_box= 0

for i in range(len(box)):
  x = box[i-1:i+1]
  if i == 0:
    continue
  elif x == "|0":
    egg_box += 1
  elif x == "||":
    emp_box += 1
  elif x == "0|":
    pass
  else:
    print("Error")

print(egg_box,emp_box)