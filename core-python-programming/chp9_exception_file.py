###In the current code as follows,we do not detect errors during the read phase(using readlines())
try:
	ccfile = open('carddata.txt', 'w')
except(IOError):
	log.write('no txns this moth\n')
txns = ccfile.readlines()
ccfile.close()
###这段代码我们不发判断是打开'carddata.txt'文件出错还是using readlines()时出错

###Looking following code
try:
	ccfile = open('carddata.txt', 'w')
	txns = ccfile.readlines()
	ccfile.close()
except(IOError):
	log.write('no txns this month\n')
#如果using readlines()时出错，就不能正常close() file

#最后一个版本：try--try--except--finally
try:
	try:
		ccfile = open('carddata.txt', 'w')
		txns = ccfile.readlines()
	except(IOError):
		log.write('no txns this month\n')
finally:
	ccfile.close()
#如果open()、readlines() file时出错就会将错误信息写入log，但不管是否出错，file都能正常关闭

#变种，但不太明白其中差异在哪
#The code works virtually the same with some differences.The most obvious one is that 
#the closing of the file happens before the exception handler writes out the error to
#the log.This is because finally automatically reraises the exception.
try:
	try:
		ccfile = open('carddata.txt', 'w')
		txns = ccfile.readlines()
	finally:
		ccfile.close()
except(IOError):
	log.write('no txns this month\n')
#finally也可以引发异常，在第三版最后close() file时出错呢？
#若选用最后的版本，close() file的错误换成其他提示，以写入log呢？
