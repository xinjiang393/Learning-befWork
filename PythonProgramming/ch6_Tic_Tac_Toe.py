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
