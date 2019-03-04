#High Scores
#演示列表方法
scores = []
choice = None
while(choice != '0'):
	print(
	"""
	\tHigh Scores
	\t0-Exit
	\t1-Show Scores
	\t2-Add a Score
	\t3-Remove a Score
	\t4-Sort Scores
	""")
	choice = input("Choice:")
	print()
	
	#退出	
	if(choice == '0'):
		print("Good-byb!")
	elif(choice == '1'):
		if(not scores):
			print("The high scores is empty at present!")
		for score in scores:
			print(score)
	elif(choice == '2'):
		score = int(input("What score did you get?:"))
		scores.append(score)
	elif(choice == '3'):
		score = int(input("Remove which score?:"))
		if(score in scores):
			scores.remove(score)
		else:
			print(score, "isn`t in the high scores list.")
	elif(choice == '4'):
		scores.sort(reverse = True)
		for score in scores:
			print(score)
	else:
		print("Sorry but", choice, "isn`t a valid choice.")
