#Guess My Number
#计算机随机挑选一个1到100的数字
#玩家尝试把它猜出来，计算机要让玩家知道猜低了还是猜高了
#或者是猜对了
import random
print("\tWelcome to 'Guess My Number'")
print("\nI`m thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

the_number = random.randint(1, 100)
guess = int(input("Take a guess:"))
tries = 1
while(guess != the_number):
	if(guess > the_number):
		print("lower...")
	else:
		print("highter...")
	guess = int(input("Take a guess:"))
	tries += 1

print("You guess it! The number was", the_number)
print("And it only took you", tries, "tries!\n")
