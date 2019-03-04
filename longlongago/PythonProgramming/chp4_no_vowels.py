#No Vowels
#演示利用for循环创建新字符串
message = input("Enter a message:")
new_message = ''
VOWELS = 'aeiou'

for letter in message:
	if(letter.lower() not in message):
		new_message += letter
		print("A new string has been created:", new_message)
print("\n\nYour message without vowels is:", new_message)
input("Press the enter key to exit.")
#
#Pizza Slicer
#演示字符串分片
word = "pizza"
print(
"""
	Slicing 'Cheat sheet'
    0   1   2   3   4
  +---+---+---+---+---+
  | P | i | z | z | a |
  +---+---+---+---+---+
   -5  -4  -3  -2  -1
"""
)
print("Enter the beginning and ending index for your slice of 'pizza'.")
print("Press the enter key at 'Begin' to exit.")
start = None
while(start != ""):
	start = input("\nstart:")
	if(start):
		start = int(start)
		finish = int(input("\nfinish:"))
		print("word[", start, ":", finish, "]is", end = " ")
		print(word[start:finish])
input("\n\nPress the enter key to exit.")
