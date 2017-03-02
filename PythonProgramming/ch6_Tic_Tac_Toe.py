#Tic_Tac_Toe
#与人类下井字棋
"""
main()流程，伪代码：
显示该游戏的操作指南----display_instruct()
决定谁先走---ask_yes_no()谁先走，pieces()玩家与电脑选好棋标识"O" or "X",nask_number()人类走哪一格，legal_moves()走合格棋
创建一个空的井字棋盘---new_board()
把棋盘显示出来---display_board()
当没人获胜且不是平局时：
		 如果轮到玩家：
		 			 得到玩家的行棋的位置---human_moves()
					 根据行棋位置更新棋盘---type(board) --->list legal_moves()
		 否则：
		 			 计算出计算机的行棋位置---for 循环遍历+legal_moves()
					 根据行棋位置更新棋盘
		 显示棋盘---display_board()
		 切换行棋方---next_turn()
向玩家表示恭喜或声明平局
"""
#全局变量
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#显示游戏说明
def dislplay_instruct():
	"""Display game instruction."""
	print(
	"""
	Welcome to the greatest intellectual challenge of all time:Tic-Tac-Toe.
	This will be a showdown between your human brain and my silicon processor.
	 
	You will make your move known by entering a number,0-8.The number will
	correspond to the board position as illustrated.
							0 | 1 | 2
							---------
							3 | 4 | 5
							---------
							6 | 7 | 8
	Prepare yourself,human.The ultimate battle is about to begin.\n
	"""
	)
	
#询问人类是否要先行棋
def ask_yes_no(question):
	"""Ask a yes or no question."""
	response = None
	while(response not in ("y", "n")):
		response = int(input(question).lower())
	return response
#指定一个范围，用于人类行棋
def ask_number(question, low, high):
	"""Ask for a number within a range."""
	response = None
	while(response not in range(low, high)):
		response = int(input(question))
	return response

#ask_yes_no() + pieces()，判断人类选X还是选O
def pieces():
	"""Determine if player or computer goes first."""
	go_first = ask_yes_no("Do you require the first move?(y/n):")
	if(go_first == 'y'):
		human = X
		computer = O
	else:
		human = O
		computer = X
	return computer, human

#显示当前棋盘
def display_board(board):
	"""Display game board on screen."""
	print("\n\t", board[0], "|", board[1], "|"，board[2] )
	print("\t", "---------")
	print("\n\t", board[3], "|", board[4], "|"，board[5] )
	print("\t", "---------")
	print("\n\t", board[6], "|", board[7], "|"，board[8], "\n" )
	
#判断合格的行棋位置
#如果某个棋格内容为空格，就说明此处可以行棋，把位置放入moves里面
def legal_moves(board):
	"""Creat list of legal moves."""
	moves = []
	for square in range(NUM_SQUARE):
		if(board[square] == empty):
			moves.append(square)
	return moves

#判断是否赢棋
#若有赢棋，则返回X，或者O
#若所有格子都有数字，且没人获胜，这返回TIE，平局
#若没人获胜，且格子还有空格empty，则返回None
def winner(board):
	"""Determine the game weinner."""
	WAY_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8)
		      (0, 3, 6), (1, 4, 7), (2, 5, 8)
		      (0, 4, 7), (2, 4, 6))
	#每个item内都是X，或者都是O
	for row in WAY_TO_WIN:
		if((board[row[0]] == board[row[1]] == board[row[2]] != EMPTY)):
			winner = board[row[0]]
			return winner
	if(EMPTY not in board):
		return TIE
	return None

#人类行棋，询问人类走哪格--得到该格位置编号--判断该编号是否为EMPTY，若不是，继续询问
def human_move(board, human):
	"""Get human move."""
	legal = legal_moves(board)  #返回是一个EMTPY位置的数字列表
	move = None
	while(move not in legal):
		move = ask_number("Where will your move?(0 - 8):", 0, NUM_SQUARE)
		if(move not in legal):
			print("\nThat square is already occupied,foolish human.Choose another.\n")
	print("Fine...")
	return move

#计算机行棋，由于共享引用，需要对board建立一个副本
#更换此方法，使计算机永不输给人类
#A：计算机走最好的位置，BEAST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
#B:遍历所有位置，看是否可赢棋
#C:遍历所有位置，看人类是否可赢棋，可，则堵死
#先B，再C，最后A
def computer_move(board, computer, human):
	"""Make computer move."""
	"""The argument of human be used to judge human will or not in next turn"""
	#最终返回一个具体的行棋位置，或者计算机赢，或者堵死人类，或者BEST_WAY
 	board = board[:]
	BEAST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	print("I shall take square number", end = ' ')
	#判断计算机是否赢棋
	for move in legal_moves(board):
		board[move] = computer
		if(winner(board) == computer):#winner() is a function, not a list.	
			print(move)
			return move
		board[move] = EMPTY
	for move in legal_moves(board):
		board[move] = human
		if(winner(board) == human):
			print(move)
			reutnr move
	for move in BEST_WAY:
		if(move in legal_moves(board)):
			print(move)
			return move

		#切换行棋方
def next_turn(turn):
	"""Switch turns."""
	if(turn == X):
		return O
	else:
		return X

#打印祝贺信息
def congrat_winner(the_winner, computer, human):
	"""Congratulate the winner."""
	if(the_winner != TIE):
		print(the_winner, "won!\n")
	else:
		print("It`s a tie!\n")
	
	if(the_winner == computer):
		print("As I predicted,human,I am triumphant once more.\n"\
		      "Proof that computers are superior to humans in all ragards.")
	elif(the_winner == human):
		print("No,no!It cannot be!Somehow you trickedme,human.\n"\
		      "But never again!I,the computer, so swear it.")
	elif(the_winner ==TIE):
		print("You were most lucky,human,and somehow managed to tie me.\n"\
		      "Celebrate today...for this the best you will ever achieve.")
#main()
def main():
	display_board()
	computer, human = piece()
	turn = X
	board = new_board()
	while(not winner(board)):
		if(turn == human):
			move = human_move(board, human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
		diesplay_board(board)
		turn = next_turn(turn)
	the_winner() = winner(board)
	congrat_winner(the_winner, computer, human)

#start main()
main()
