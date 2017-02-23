#Global Scope Versue Local Scope with nested function
#演示全局变量与局部变量

def foo():
	m = 3
	def bar():
		n = 4
		print(m + n)
		print("This is global scope of foo() within bar():", m)
	print("This is global scope of foo() without bar():", m)
	bar()

>>>foo()
This is global scope of foo() without bar():3
7
This is global scope of foot() within bar():3

def foo():
	m = 3
	def bar():
		n = 4
		print(m + n)
		print("This is global scope of foo() within bar():", m)
	try:
		print("This is local scope of bar() within bar():", n)
	except:
		bar()
		
>>>foo()
7
This is global scope of foo() within bar():3
	
"""
If references are made from inside an inner function to an object defined in any outer scopre
(but not in the global scope),the inner function then is known as a closure.The variables defined 
in the outer function but used or referenced to by the inner function are called free variable
"""

def counter(start_at = 0):
	count = [start_at]
	def incr():
		count[0] += 1
		return count[0]
	return incr
>>>co = couter(5)
>>>co()
6

def counter_new(start_at = 0):
	count = start_at
	print(count)
	def incr():
		count += 1
		return count
	return incr
>>>cou = couter_new(5)
5
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in incr
UnboundLocalError: local variable 'count' referenced before assignment
cout的类型是int和list有什么不同？？
"""
