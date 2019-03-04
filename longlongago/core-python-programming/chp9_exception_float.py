>>>float("foo")
Traceback (innermost last):
	File"<stdin>", line 1, in?
		float('foo')
ValueError:invalid literal for float():foo

def start_float(obj):
	try:
		return float(obj)
	except(ValueError):
		pass
		
#自主定义返回的错误信息
def start_float_1(obj):
	try:
		retval = float(obj)
	except(ValueError):
		retval = 'Couldn`t convert non-number to float'
	return retval
	
>>>start_float_1("foo")
Couldn`t convert non-number to float


def start_float_2(obj):
	try:
		retval = float(obj)
	except(ValueError):
		retval = "Couldn`t convert non-number to float"
	except(TypeError):
		retval = "object type cannot be converted to float"
	return retval

>>>dic = {"name":"hello", "type":"dictionary"}
>>>start_float_2(dic)
'object type cannot be converted to float'

#except statement with multiple exception
def start_float_3(obj):
	try:
		retval = float(obj)
	except(ValueError, TypeError):
		retval = "argument must be a numver or numberic string"
	return retval
	
>>>start_float_3(dic)
"argument must be a number or numberic string"
