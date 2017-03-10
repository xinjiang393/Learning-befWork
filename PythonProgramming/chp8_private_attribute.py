#类的私有属性、私有方法
class Critter(object):
	def __init__(self, name, mood):
		print("A new critter has been born!")
		self.name = name	#public attribute
		self.__mood = mood	#private attribute
		
	def talk(self):
		print("Right now I feel", self.__mood, '\n')	#accessing private attribute
	
	def __private_method(self):
		print("This is a private method.")
	def public_method(self):
		print("This is a public method.")
		self.__private_method()	#从类的内部调用私有方法
>>>cri = Critter(name = 'yuri', mood = 'happy')
'A new critter has been born!'
>>>cri.__private_method()
Traceback(most recent call last):
	File"<pyshell#l>", line 1, <module>
AttributeError:'Critter' object has no attribute '__private_method'

#1.类的私有属性和类是不能通过实例名访问，可以通过类名访问，或者类的其他方法调用私有方法、私有属性
#2.某些类的属性是一旦建立就不能再修改，此时应该设置为只读，@property
#3.将属性设置成setter，变成可读写
class Critter(object):
		'''A virtual pet.'''
		def __init__(self, name):
			print("A new critter has been born!")
			self.__name = name
		@property
		def name(self):
			return self.__name
>>>cri = Critter(name = 'hello')
A new critter has been born!
>>>cri.name
'hello'
>>>cri.name = 'world'
Traceback(most recent call last):
	File"<pyshell#l>", line 1, <module>
AttributeError:can`t set attribute

class New_Critter(object):
	def __init__(self, name):
		print("A new critter has been born!")
		self.__name = name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self, new_name):
		if(new_name == ''):
			print("A critter`s name can`t be the empty string.")
		else:
			self.__name = new_name
			print("Name change successful!")
>>>Ncri = New_Critter(name = 'haha')
A new critter has been born!
>>>Ncri.name
'haha'
>>>Ncri.name = 'HAHA'
>>>Ncri.name
'HAHA'
#4.attribute.setter属性可以控制私有属性的修改、访问，一般会与@property连用
