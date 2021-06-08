curr=int(input())
distinct_num = 1
while ( curr != -1 ):
  prev = curr
  curr=int(input())
  if ( prev != curr and curr != -1):
    distinct_num += 1
print(distinct_num)