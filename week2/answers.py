Ppa 1

x=int(input())
if x<10 and x>0:
    print(float(x+2))
elif x>=10:
    print(float(x*x+2)) 
else:
    print(0)

Ppa 2
x=float(input())
y=float(input())
if(x==0 and y==0):
    print('Origin')
elif(x==0 and y!=0):
    print("Y-axis")
elif(y==0 and x!=0):
    print("X-axis")
elif(x>0 and y>0):
    print("I")
elif(x>0 and y<0):
    print("IV")
elif(x<0 and y>0):
    print("II")
else:
    print("III")

Ppa3 
x1,y1,x2,y2,x3=float(input()),float(input()),float(input()),float(input()),float(input())
if(x2==x1):
    print('Vertical Line')
else:
    y3=((x3-x1)*(y2-y1)/(x2-x1)+y1)
    print(y3)
    slope=(y2-y1)/(x2-x1)
    if slope>0:
        print("Positive Slope")
    elif slope<0:
        print("Negative Slope")
    else:
        print("Horizontal Line")

Ppa4

x=input()
if len(x)%2==0:
    if x[-1]=="." :
        x=x[0:-1]
    elif x[-1]!=".":
        x=x+"."

y=int(len(x)/2)

print(x[y-1]+x[y]+x[y+1])

Ppa5


x,y,z=input(),input(),input()

if x=='True' and y == z =='False':
    print("True")
else:
    print(z)

Gpa1

x,y,z=int(input()),int(input()),int(input())
if((x+y>z) and (y+z>x) and (z+x>y)):
    print("YES")
else:
    print("NO")

Gpa2
x=int(input())
if(x<0):
    print("INVALID")
if 0<=x and x<=5:
    print("NIGHT")
if 6<=x and x<=11:
    print("MORNING")
if 12<=x and x<=17:
    print("AFTERNOON")
if 18<=x and x<=23:
    print("EVENING")
if x>=24:
    print("INVALID")

Gpa3


a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
if(a%2==0 and b%2==0 and c%2==0 and d%2==0 and e%2==0)or(a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0 and e%2!=0):
    print("YES")
else:
    print("NO")

Gpa4

x=input()
x=x.lower()
t=""
if 'a'in x:
    t+='a'
if 'e'in x:
    t+='e'
if 'i' in x:
    t+='i'
if 'o' in x:
    t+='o'
if 'u' in x:
    t+='u'
print(t)

Gpa5

x,xdob,y,ydob=input(),input(),input(),input()

xd=int(xdob[0]+xdob[1])
xm=int(xdob[3]+xdob[4])
xy=int(xdob[6]+xdob[7]+xdob[8]+xdob[9])
yd=int(ydob[0]+ydob[1])
ym=int(ydob[3]+ydob[4])
yy=int(ydob[6]+ydob[7]+ydob[8]+ydob[9])
if(xy>yy):
    print(x)
elif(yy>xy):
    print(y)
else :
    if xm>ym:
        print(x)
    elif ym>xm:
        print(y)
    else:
        if xd>yd:
            print(x)
        elif yd>xd:
            print(y)
        else:
            print(min(x,y))

Gpa6

x=input()
q=len(x)>7 and len(x)<33
y=(x[0].isalpha())
r=not(('/'in x) or ("\\"in x) or ("=" in x) or("'"in x) or('"'in x) or(" "in x))

if (((q and y) and r)):
    print("True")
else:
    print("False")