#Maitre`d
#演示将值看作条件
print("Welcome to the Chateau D`Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre`D?"))

if(money):
  print("Ah, I am reminded of a table.Right this way.")
else:
  print("Please, sit. It may be a while.")
  
input("\n\nPress the enter key to exit.")

#Finicky Counter
#演示break和continue
count = 0
while(True):
  count += 1
  #count大于10就结束循环
  if(count > 10):
    break   #break语句会结束当前的循环体
  #跳过5
  if(count == 5):
    continue    #continue是跳到当前循环的开头，判断while语句中的条件--->执行循环体语句
  print(count)
