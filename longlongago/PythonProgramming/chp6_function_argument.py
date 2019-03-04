#Birthday Wishes
#演示关键字参数和默认参数值

#position argument
def birthday1(name, age):
	print('Happy birthday,', name, '!', 'I hear your`re', age, 'today.\n')

>>>birthday1('Jackson', 1)
Happy birthday,Jackson!I hear you`re 1 today.
>>>birthday1(1, 'Jackson')
Happy birthday, 1!I hear you`re Jackson today.
>>>birthday1(name = 'Jackson', age = 1)
Happy birthday,Jackson!I hear you`re 1 today.
>>>birthday1(age = 1, name = 'Jackson')
Happy birthday,Jackson!I hear you`re 1 today.

#default value argument
def birthday2(name = 'Jackson', age = 1):
	print("Happy birthday," name, '!', "I hear you`re", age, 'today.\n')
>>>birthday2()
Happy birthday,Jackson!I hear you`re 1 today.
>>>birthday2(name = 'Katherine')
Happy birthday, Katherine!I hear you`re 1 today.
>>>birthday2(age = 12)
Happy birthday, Jackson!I hear you`re 12 today.
>>>birthday2(name = "Katherine", age = 12)
Happy birthday,Katherine!I hear you`re 12 today.
>>>birthday2("Katherine", 12)
Happy birthday, Katherine!I hear you`re 12 today.
>>>birthday2(12, "Katherine")
Happy birthday, 12!I hear you`re Katherine today.
