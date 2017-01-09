import string
"""
Import string module,so that we can deal with some problem about alphanumeric
"""

__python_version__ = 3.6.0

###get alphanumeric
alph = string.ascii_letter ##python2.6:string.letter python3.0:string
###get number
num = string.ascii_digits

print("Welcome to the Identifier Checker V1.0")
print("Testes must be at least char 2 long.")
myput = input("Identify to test?")

if(len(myput) > 1):   #Ensure the lenght of myput must be greater than 2
  if(myput[0] not in alph):     #Ensure the first item can`t be number.
    print("invalid:first symbol must be alphabetic.")
  esle:
    for otherchar in myput[1:]:
      if(otherchar not in alph + num):    #Judge items of the string including special character or not.
        print("invalid:first symbol must be alphnumric")
        break
    esle:
      print("Okey as an identifier.")
