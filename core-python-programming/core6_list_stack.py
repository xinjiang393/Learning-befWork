"""
This simple scipt uses lists as a stack to store and retrive strings entered through
this menu-driven text application using only the append() and pop() list methods.
"""
___PythonVersion__ = 3.6.1

stack = [] #Defining lists as a stack to store strings.

def pushit():
  """Push items into stack. """
  stack.append(input(Enter new string:).strip())

def popit():
  """Pop items from stack"""
  if(len(stack) == 0):
    print("Cannot pop from an empty stack!")
   else:
    print("Removed [%s]" % stack.pop())
    
def viewstack():
  """Display the detail of stack. """
  print(stack)
  
#It is convient that end user choice stack methods
#through the keys of dictionary.
CMDs = {'u':pushit, 'o':pupit, 'v':viewstack}

def showmenu():
  """Show operating methods to end user."""
  pr = """
  p(U)sh
  p(O)p
  (V)iew
  (Q)uit
  Enter choice:
  """
  while(True):
    while(True):
      try:
        choice = input(pr).strip()[0].lower()
      except(EOFError, KeyboarInterrupt, IndexError):
        choice = 'q'
      print("\nYou picked:[%s]" % choice)
      if(choice not in 'uovq'):
        print("Invaild option, try again")
      else:
        break
    if(choice == 'q'):
      break
    CMDS[choice]()  #Different 'choice' can call different methods by using dictionary

if(__name__ == '__main__'):
  showmenu()
  
  
  
"""
The result of this programs are as follows:
Enter new string: who are u?

        p(U)sh
        p(O)p
        (V)iem
        (Q)uit
        Enter choice:
        v

You picked:[v]
['hello', 'hello world', 'who are u?']

        p(U)sh
        p(O)p
        (V)iem
        (Q)uit
        Enter choice:
        q

You picked:[q]

"""
