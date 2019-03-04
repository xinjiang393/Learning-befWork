#Global Reach
#演示全局变量
def read_global():
	print("From inside the local scope of read_global(), value is:", value)
def shadow_global():
	value = -10
	print("From inside the local scope of shadow_global(), value is:", value)
def change_global():
	global value
	value = -10
	print("From inside the local scope of change_global(), value is:", value)

>>>value = 10
10
>>>read_global()
From inside the local scope of read_global(), value is:10
>>>shadow_global()
From inside the local scope of shadow_global, value is:-10
>>>print("Back in the global scope,value is still:", value, "\n")
Back in the global scope, value is still:10
>>>change_global()
-10
>>>print("Back in the global scope, value has now changed to:", value)
Back in the global scope, value has now changed to:-10
>>>read_global()
From inside the local scope of read_global(),value is:-10

####在函数中全局变量可不是什么好习惯，这可能会引起一些理解方面的问题，并且也很难对它们的值进行跟踪。
####全局常量却相反，更加有利于改善可读性。当经常使用一个常数时，当设置全局常量如：TAX_RATE，全大写
####这在日后的维护、修改也不至于太费劲
