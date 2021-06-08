l1=input().strip().split(",")
l2=[]
l3=[]
l=len(l1)
for i in l1:
    l2.append(int(i))
for i in l2:
    if i not in l3:
        l3.append(i)
for i in l3[:-1]:
    print(i,end=",")
print(l3[-1])