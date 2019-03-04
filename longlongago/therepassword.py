valid = False
count = 3
while(count > 3):
  pass_input = input("enter password:")
  #check for valid password
  for eachPassword in PasswordList:
    if(pass_input == eachPassword):
      valid = True
      break
  if(not valid):
    print("invalid input")
    count -= 1
    continue
  else:
    break

#Find largest factor of the number
def showMaxFactor(num):
  count = num / 2
  while(count > 0):
    if(num % count == 0):
      print("Largest factor of %d is %d" % (num, count))
      break
    count -= 1
  else:
    print(num, "is prime")
 
for eachnum in range(10, 21):
  showMaxFactor(eachnum)
