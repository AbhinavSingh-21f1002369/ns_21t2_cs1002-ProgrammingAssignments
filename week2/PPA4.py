print("PPA4")

string = input()

def midchar(string):
  length = len(string)
  mid_index = length//2
  return(string[mid_index-1:mid_index+2])

if len(string)%2 == 0 :
  if string[-1]=='.':
    string = string.rstrip(".")
  else:
    string = string + "."
  print(midchar(string))
else :
  print(midchar(string))