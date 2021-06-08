n=input().strip().split(" ")
l=[]

total=0
for i in n:
    l.append(int(i))
    total+=int(i)
l.sort()
average=total/len(n)
for i in range(len(l)):
    if l[i]>average and i!=len(l)-1:
        print(l[i],end=" ")
    elif l[i]>average and i==len(l)-1:q
        print(l[i])