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
