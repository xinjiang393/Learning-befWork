### Django设置数据库
- 安装MySQL的connector
    * pip3 install mysqlclient
- 设置数据库连接信息
    * vim HelloWorld/HelloWorld/settings.py
    * 如果Host=localhost，是会报错的
```
DATABASES = {
        'default':{
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mall',
            'USER': 'duser',
            'PASSWORD': '1Dk*I@T#!iZY',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        },
}
```
- Django规定使用模型需要创建APP
    * django-admin startobject TestModel

- vim HelloWorld/TestModel/models.py
    * Test就表示mall这个库中的一个表，而name是这个表的某个字段
```
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)
    
    
$ python manage.py migrate   # 创建表结构
$ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate TestModel   # 创建表结构
```

- 创建完表结构，可以查看是否有这张表
```
mysql> use mall;
mysql> show tables;
+----------------------------+
| Tables_in_mall             |
+----------------------------+
| TestModel_test             |
+----------------------------+
```

- 修改HelloWorld/HelloWorld/urls.py。下次runserver，可以访问`$testdb`
```
from django.conf.urls import *
from . import view,testdb
 
urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
]
```

### 数据库的相关操作
```
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from TestModel.models  import Test

'''
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>Adding datas successfully!</p>")
'''

def testdb(request):
    response = ''
    response1 = ''

    list = Test.objects.all()
    response2 = Test.objects.filter(id=1)
    response3 = Test.objects.get(id=1)
    Test.objects.order_by('name')[0:2]

    Test.objects.order_by('id')
    Test.objects.filter(name='runoob').order_by('id')

    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    test2 = Test.objects.get(id=2)
    test2.delete()

    for var in list:
        response1 += var.name + ' ^_^ '
    response = response1
    #response = response1 + " @_@ " + response2 + " ^_^ " + response2
    return HttpResponse("<p>" + response + "</p>")
```