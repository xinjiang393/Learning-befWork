#Version 2.0 Of High Score
#演示嵌套列表
scores = []
choice = None
while(choice == '0'):
	print(
	"""
	\tHigh Score 2.0
	\t0-Quit
	\t1-List Scores
	\t2-Add a Scores
	""")
	#Exit
	if(choice == '0'):
		print("Good-byb！")
	elif(choice == '1'):
		print("\nHigh Score")
		print("Name\tScore")
		for entry in scores:
			score, name = entry
			print(name, "\t", score)
	elif(choice == '2'):
		name = input("Which is the player`s name?:")
		score = int(input("What score did the player get?:"))
		entry = (score, name)
		scores.append(entry)
		scores.sort(reverse = True)
		scores = scores[:5]		#只保留最高的5条记录
	#elif(choice == '3'):  用于以后删除分数
	else:
		print("Sorry,but",choice, "isn`t a valid choice!")
