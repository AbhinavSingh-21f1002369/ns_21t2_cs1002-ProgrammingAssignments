a_name = input()
a_dob = input()
b_name = input()
b_dob = input()

a_date = int(a_dob[0:2])
a_month = int(a_dob[3:5])
a_year = int(a_dob[6:10])
b_date = int(b_dob[0:2])
b_month = int(b_dob[3:5])
b_year = int(b_dob[6:10])

if a_dob == b_dob:
    if a_name>b_name:
      print(b_name)
    else:
      print(a_name)
else:
  if a_year>b_year:
    print(a_name)
  elif a_year==b_year:
    if a_month>b_month:
      print(a_name)
    elif a_month==b_month:
      if a_date>b_date:
        print(a_name)
      else:
        print(b_name)
    else:
      print(b_name)
  else:
    print(b_name)