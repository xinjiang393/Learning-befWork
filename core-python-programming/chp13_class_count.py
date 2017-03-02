class InstCt(object):
	count = 0
	def __init__(self):
		InstCt.count += 1
	def __del__(self):
		InstCt.count -= 1
	def howMany(self):
		print(InstCt.count)

>>>b = InstCt()
>>>b.howMany()
1
>>>a = InstCt()
>>>b.howMany()
2
>>>del b
>>>a.howMany()
1
>>>del a
>>>InstCt.count
0


#Instance attributes VS class attributes
#for immutable attributes
class Foo(object):
	x = 1.5	
>>>foo = Foo()
>>>foo.x = 1.7
>>>foo.x
1.7
>>>Foo.x
1.5
>>>del foo.x
>>>foo.x
1.5

#for mutable attributes
class Bar(object):
	x = {2003:"poe2"}	
>>>bar = Bar()
>>>bar.x
{2003:"poe2"}
>>>bar.x[2004] = "valid path"
>>>bar.x
{2003:"poe2", 2004:"valid path"}
>>>Bar.x
{2003:"poe2", 2004:"valid path"}
>>>id(bar.x) == id(Bar.x)
True
