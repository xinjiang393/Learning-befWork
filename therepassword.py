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
