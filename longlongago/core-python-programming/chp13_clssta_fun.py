#比较staticmethod和classmethod，以及generalmethod的区别
class Test(boject):
  def instanceFun(self):
    print("instance function")
    print(self)
  
  @classmethod
  def classFun(self):
    print("class function")
    print(self)
    
  @staticmethod
  def staticFun():
    print("static function")
  
  def function():
    print("general function")

>>> t = Test()
>>> t.instanceFun()
instance function
>>> t.classFun()
class function
<class '__main__.Test'>
>>> t.staticFun()
static function
>>>
>>> t.function()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() takes 0 positional arguments but 1 was given
###因为general function()没有参数self,所以"实例t"无法调用它，但是类可以，Test.function()

>>> Test.instanceFun()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: instanceFun() missing 1 required positional argument: 'self'
>>> Test.classFun()
class function
<class '__main__.Test'>
>>> Test.staticFun()
static function
>>> Test.function()
general function
###"类Test"可以调用普通函数，但是实例函数需要带参数
>>> Test.instanceFun(t)
instance function
>>> Test.instanceFun(Test)
instance function
"""
总结：
1："实例t"不能调用不带self参数的普通方法，其他都可以
2：classmethod带参数self，而staticmethod不带参数
3："实例t"和"类Test"都可以调用classmethod()和staticmethod()
4："类Test"调用instanceFunction()需要带参数
5：有参数self为实例函数，没有参数self的为普通函数，@标识符是装饰器，说明静态或类方法
"""
