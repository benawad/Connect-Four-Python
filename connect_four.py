class ConnectFour(object):

	def __init__(self):
		self.p1 = 'X'
		self.p2 = 'O'
		self.board = [[' ']*7 for i in range(6)]

	def to_string(self):
		sBoard = ''
		for row in self.board:
			for section in row:
				sBoard +=  "( %s )" % section
			sBoard += '\n-----------------------------------\n'

		sBoard += '  0    1    2    3    4    5    6'
		return sBoard

	def turn(self, player):
		if (player == self.p1):
			while True:
				col = int(raw_input('p1>'))
				if (self.board[0][col] == ' '):
					break
		else:
			while True:
				col = int(raw_input('p2>'))
				if (self.board[0][col] == ' '):
					break

		row_count = 5
		for row in reversed(self.board):
			if (row[col] == ' '):
				self.board[row_count][col] = player
				break
			row_count -= 1

		print self.to_string()

	def diagonal(self, player):
		for row in range(len(self.board)):
			for hole in range(len(self.board[row])):
				if (row - 3 > -1 and hole - 3 > -1):
					try:
						if (self.board[row][hole] == player and self.board[row-1][hole-1] == player and self.board[row-2][hole-2] == player and self.board[row-3][hole-3] == player):
							self.board[row][hole] = self.board[row][hole].lower()
							self.board[row-1][hole-1] = self.board[row-1][hole-1].lower()
							self.board[row-2][hole-2] = self.board[row-2][hole-2].lower()
							self.board[row-3][hole-3] = self.board[row-3][hole-3].lower()
							print self.to_string()
							return True
					except:
						pass

		for row in range(len(self.board)):
			for hole in range(len(self.board[row])):
				if (row-3 > -1):	
					try:
						if (self.board[row][hole] == player and self.board[row-1][hole+1] == player and self.board[row-2][hole+2] == player and self.board[row-3][hole+3] == player):
							self.board[row][hole] = self.board[row][hole].lower()
							self.board[row-1][hole+1] = self.board[row-1][hole+1].lower()
							self.board[row-2][hole+2] = self.board[row-2][hole+2].lower()
							self.board[row-3][hole+3] = self.board[row-3][hole+3].lower()
							print self.to_string()
							return True
					except:
						pass

		return False

	def horizontal(self, player):
		for row in range(len(self.board)):
			for hole in range(len(self.board[row])):
				try:
					if (self.board[row][hole] == player and self.board[row][hole+1] == player and self.board[row][hole+2] == player and self.board[row][hole+3] == player):
						self.board[row][hole] = self.board[row][hole].lower()
						self.board[row][hole+1] = self.board[row][hole+1].lower()
						self.board[row][hole+2] = self.board[row][hole+2].lower()
						self.board[row][hole+3] = self.board[row][hole+3].lower()
						print self.to_string()
						return True
				except:
					pass

		return False

	def vertical(self, player):
		for row in range(len(self.board)):
			for hole in range(0, len(self.board[row])):
				if (row - 3 > -1):
					try:
						if (self.board[row][hole] == player and self.board[row-1][hole] == player and self.board[row-2][hole] == player and self.board[row-3][hole] == player):
							self.board[row][hole] = self.board[row][hole].lower()
							self.board[row-1][hole] = self.board[row-1][hole].lower()
							self.board[row-2][hole] = self.board[row-2][hole].lower()
							self.board[row-3][hole] = self.board[row-3][hole].lower()
							print self.to_string()
							return True
					except:
						pass

		return False

	def is_winner(self, player):
		if (self.diagonal(player) == True or self.horizontal(player) == True or self.vertical(player) == True):
			return True, False
		if ( self.board[0][0] != ' ' and self.board[0][1] != ' ' and self.board[0][2] != ' ' and self.board[0][3] != ' ' and self.board[0][4] != ' ' and  self.board[0][5] != ' ') and self.board[0][6] != ' ':
			return False, True

		return False, False

	def start(self):
		print self.to_string()
		while True:
			self.turn(self.p1)
			win, draw = self.is_winner(self.p1)
			if(win == True):
				print "Winner:", self.p1
				break
			elif(draw == True):
				print "Draw"
				break
			self.turn(self.p2)
			win, draw = self.is_winner(self.p2)
			if(win == True):
				print "Winner:", self.p2
				break
			elif(draw == True):
				print "Draw"
				break