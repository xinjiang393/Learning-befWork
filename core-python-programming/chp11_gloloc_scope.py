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
