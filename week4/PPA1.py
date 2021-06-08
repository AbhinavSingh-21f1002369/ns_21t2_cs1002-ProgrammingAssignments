units = int(input())
bill = 0
if units > 500:
    bill += 5*100 + 300*8 + (units-500)*10
elif units > 200:
    bill += 5*100 + (units-200)*8
elif units > 100:
    bill += 5*(units-100)
else:
    pass
print(bill)