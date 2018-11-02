# tic tac toe


class Board:

	def __init__(self):
		self.board = [["-" for _ in range(3)] for _ in range(3)]
		self.empty_spot = {(row, col) for row in range(3) for col in range(3)}

	def add_token(self, player):
		icon, pos = player.icon, player.pos
		self.board[pos[0]][pos[1]] = icon
		self.empty_spot.remove((pos[0], pos[1]))

	def print_board(self):
		for row in self.board:
			print("|".join(row))
		print("\n")

	def is_full(self):
		return not self.empty_spot

class AI_Player:
	def __init__(self, pos):
		self.icon = "O"
		self.pos = pos

	def dumb_move(self, board):
		if board.is_full():
			raise Exception("Board is full, no leagal move")
		move = list(board.empty_spot)[0]
		self.pos = move
		board.add_token(self)
		return move

class Human_player:
	def __init__(self, pos):
		self.icon = "X"
		self.pos = pos

	def move(self, board):

		coordinate = None
		while True:
			coordinate_input = input("Insert your move as [row, col]:")
			row, col = coordinate_input.split(",")
			row, col = int(row), int(col)
			if (row, col) in board.empty_spot:
				coordinate = [row, col]
				break
			else:
				print("Not legal move, try again")
		self.pos = coordinate
		board.add_token(self)

class Game:

	def __init__(self):
		self.board = Board()
		self.human_player = Human_player(None)
		self.ai_player = AI_Player(None)

	def play(self):

		while not self.board.is_full():
			self.human_player.move(self.board)
			self.ai_player.dumb_move(self.board)
			self.board.print_board()

# board = Board()
# board.print_board()
#
# # add token
# ai_player = AI_Player([1,1])
#
# board.add_token(ai_player)
# board.print_board()
#
# # test ai all move
# while True:
# 	ai_player.dumb_move(board)
# 	board.print_board()
game = Game()
game.play()