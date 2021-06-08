x=input()
q=len(x)>7 and len(x)<33
y=(x[0].isalpha())
r=not(('/'in x) or ("\\"in x) or ("=" in x) or("'"in x) or('"'in x) or(" "in x))

if (((q and y) and r)):
    print("True")
else:
    print("False")