s = input()
o = '({['
c = ')}]'
b = ''
match = True
for i in s:
    if i in o:
        b = b+i
    if i in c:
        if o[c.index(i)] in b and o[c.index(i)] == b[-1]:
            b = b[:-1]
        else:
            match = False
            break
if len(b) != 0:
    match = False
print(match)