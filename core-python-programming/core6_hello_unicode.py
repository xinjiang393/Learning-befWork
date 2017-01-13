"""
An example of reading and writing Unicode string:Writes a 
Unicode string to a file in utf-8 and read it back in.
"""


CODEC = 'utf-8'  #需要编码的格式
FILE = 'unicode.txt'  #字符串写入的文件

hello_out = u'hello word'
bytes_out = hello_out.encode(CODEC)

#讲字符串以byte的格式写入到'unicode.txt'中
with open(FILE, 'w') as f:
  f.write(bytes_out)

#讲文件内容打印至屏幕

with open(FILE, 'r')  as f:
  bytes_in = f.read()
  hello_in = bytes_in.decode(CODEC)
print(hello_in)
"""
注：在Python3.6.1中，line15会报错：write() argment must be str, not bytes
"""
