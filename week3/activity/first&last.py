n = int(input("Enter any number: "))
x = n
last_digit = n % 10
first_digit = 0
while(n > 0):
    first_digit = n % 10
    n = n // 10
print("first digit is: ",first_digit)
print("last digit is: ",last_digit)