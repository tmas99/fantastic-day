# See page 13-14

import sys # Used for the sys.exit function

target_int = raw_input("How many intergers?")

try:
    target_int = int(target_int)
except ValueError:
    sys.exit("You must enter an integer")

ints = list()

count = 0
#print(str(target_int))

while count < target_int:
   new_int = raw_input("Please enter integer {0}:".format(count+1))
   isint = False
   try:
      new_int = int(new_int)
      isint = True
   except:
      print("You must enter an integer")

   if isint == True:
      ints.append(new_int)
      count += 1

print("Using a for loop")
for value in ints:
    print(str(value))

print("Using a while loop")
total = len(ints)
count = 0
while count < total:
    print(str(ints[count]))
    count +=1
