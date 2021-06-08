asc_sort=True
desc_sort=True
curr=int(input())
while ( curr != -1 ):
  prev = curr
  curr=int(input())
  if ( curr != -1 and prev > curr and asc_sort == True) :
    asc_sort=False
  if (curr != -1 and prev < curr and desc_sort == True) :
    desc_sort=False
if asc_sort==True:
  print('asc')
elif desc_sort==True:
  print('desc')
else:
  print('False')