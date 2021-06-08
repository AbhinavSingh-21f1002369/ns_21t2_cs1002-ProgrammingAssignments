l1 = input()
count = 0
sum = 0
ml=[]
while l1 != "END":
  ml.append(float(l1))
  sum += float(l1)
  count += 1
  l1=input()
print(count,sum,ml)
avg = sum / count
# the main loop starts here....
print(avg)
total=0
for i in ml:
  total = total + (i - avg)**2

print(total)
total = total / count - 1
print(total)
sd = total**0.5
print(sd)
print(f'2.74')

'''
S, l = 0, []
x = input()
while x != 'END':
    l.append(float(x)) 
    x = input()
if len(l) > 1:
    avg = sum(l) / len(l)
    for i in l:
        S += (i-avg)**2
    SD = (S / (len(l)-1))**0.5
    print(f'{SD:.2f}')
'''