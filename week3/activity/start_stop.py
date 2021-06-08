start, stop = int(input()), int(input())

for i in range(start,stop+1):
  if i%3 == 0 and i%5 == 0 and i%10 == 0 :
    break
  elif (i%3 == 0 and i%5 == 0) or (i%10 == 0 and i%5 == 0) or (i%3 == 0 and i%10 == 0) :
    pass
  elif i%3 == 0 :
    print("Divisible by 3")
  elif i%5 == 0 :
    print("Divisible by 5")
  elif i%10 == 0 :
    print("Divisible by 10")
  else:
    print(i)