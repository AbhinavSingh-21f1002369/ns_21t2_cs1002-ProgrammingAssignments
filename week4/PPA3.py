message1 = input()
alp = "abcdefghijklmnopqrstuvwxyz"
nm = "0123456789"
message2 = "";
for i in message1:
    if i.isalpha() == True:
        if i.isupper() == True:
            index = alp.index(i.lower())
            message2 += (alp[25-index]).upper()
        else:
            index = alp.index(i)
            message2 += (alp[25-index])
    elif i.isdigit() == True:
        index=nm.index(i)
        message2 += (nm[9-index])
    elif i == " ":
        message2 += "_"
    else:
         message2 += i
print(message2)