x = float(input())
y = float(input())

if x==0 and y==0 :# defines origin
  print("Origin")
  
elif x==0 and y!=0 :# defines Y-axis
  print("Y-axis")

elif x!=0 and y==0 :#defines X-axis
  print("X-axis")

else:#defines Quadrant

  if x>0 and y>0:
    print("I")
  elif x<0 and y>0:
    print("II")
  elif x<0 and y<0:
    print("III")
  else:
    print("IV")