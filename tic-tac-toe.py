"""
Tic Tac Toe Simulation Starter Code
"""
import random

class TicTacToeSim:
	board=[]
	AI=False
	turn=1
	AITurn=1
	# Part 1
	def __init__(self):
		#initialising a 2d list with zeros for our board
		for i in range(3):
			self.board.append([])
			for j in range(3):
				self.board[i].append(0)
		temp="" #making a temporary variable for user input
		while True: #input valdidation for first user input
			temp=input("Would you like to play against AI? (True/False): ")
			if(temp=="True" or temp=="False"):
				break
		if(temp=="True"): #Storing user input in AI variable
			self.AI=True
		if(self.AI): #asking user for first player in case of AI play
			while True: #input validation for user choice
				temp=input("Would you like to be player 1 or 2? 1/2: ")
				if(temp=="1" or temp=="2"):
					break	
			if(temp=="1"): #storing user choice in variable AITurn
				self.AITurn=2
			else:
				self.AITurn=1
		return

	def change_turn(self):
		#toggling current player
		if(self.turn==1):
			self.turn=2
		else:
			self.turn=1
		return

	def play_game(self):
		#driver for game
		print("Player 1 goes first.")
		while True:	#infinite loop so that game keeps on going
			if(self.AI and self.turn==self.AITurn): #calling smart_move function in case of AI turn 
				self.smart_move()
			else: #printing board and asking for coordinates for user
				self.print_board()
				self.take_turn(self.turn)
			
			if(self.check_winner()==-1): #checking if the game has reached a draw
				print("\nIt's a draw.")
				self.print_board()
				break
			elif(self.check_winner()==self.turn): #checking if any player has won
				print("\nPlayer %d wins." %self.turn)
				self.print_board()
				break

			self.change_turn() #toggling player for next turn
			print()
		return

	# Part 2
	def print_board(self):
		# printing the board in a user-readable form
		for i in range(3):
			print("[", end="")
			for j in range(3):
				print('\'', end="")
				if (self.board[i][j]==0):
					print(' ', end="")
				elif (self.board[i][j]==1):
					print('X', end="")
				else:
					print('O', end="")
				print('\'', end="")
				if(j!=2):
					print(", ", end="")
			print(']')
		return

	# Part 3
	def get_move(self):
		# Get input from user asking for their move as a tuple
		temp=""
		while True: #input validation for input row
			temp=input("Row: ")
			if(int(temp)>=0 and int(temp)<=2):
				break
		temp2=""
		while True: #input validation for input column
			temp2=input("Column: ")
			if(int(temp2)>=0 and int(temp2)<=2):
				break
		tup=(int(temp), int(temp2))	#storing user input in a tuple
		return tup

	# Part 4
	def take_turn(self, player):
		# This is the driver method for a players turn
		print("It is player %d's turn" %self.turn)
		print("Which move would you like to make?")
		while True: #checking if user input coordinates aren't already used by a player
			tup=self.get_move()
			templist=self.get_available_squares()
			for i in range(len(templist)):
				if(tup==templist[i]):
					self.make_move(tup, player)
					return

	def get_available_squares(self):
		# Get a list of available squares as tuples (row,col)
		avail=[] 
		for i in range(3):
			for j in range(3):
				if(self.board[i][j]==0):
					tup=(i, j)
					avail.append(tup)
		return avail

	def make_move(self, move, player):
		self.board[move[0]][move[1]]=player #marking board with 0/1 according to current player
		return

	# Part 5
	def check_winner(self):
		for i in range(3):
			countr=0
			countc=0
			for j in range(3):
				if(self.board[i][j]==self.turn):
					countr+=1 #checking if the same player has marked a whole row
				if(self.board[j][i]==self.turn):
					countc+=1 #checking if the same player has marked a whole column
			if(countr==3 or countc==3):
				return self.turn #returning winner if player has marked a whole column/row
		if(self.board[0][0]==self.turn and self.board[1][1]==self.turn and self.board[2][2]==self.turn):
			return self.turn #returning winner if player has marked first diagonal
		if(self.board[0][2]==self.turn and self.board[1][1]==self.turn and self.board[2][0]==self.turn):
			return self.turn #returning winner if player has marked second diagonal

		for i in range(3):
			if(0 in self.board[i]):
				return 0 
		return -1 #returning draw in case the whole board is filled and there is no winner

	# Part 6
	def make_random_move(self):
		templist=self.get_available_squares()
		return random.choice(templist) #returning random move from list of available moves

	# Part 7
	def winning_move(self, player):
		# Find a winning move for a player
		templist=self.get_available_squares()
		for t in range(len(templist)): #checking for all available moves
			tempboard=[] #creating a temporary deep copy of main board
			for i in range(3):
				tempboard.append([])
				for j in range(3):
					tempboard[i].append(self.board[i][j])

			tempboard[templist[t][0]][templist[t][1]]=player #marking each move to temporary board
			#checking if AI can win with the particular move and returning if there is any 
			for i in range(3):
				countr=0
				countc=0
				for j in range(3):
					if(tempboard[i][j]==player):
						countr+=1
					if(tempboard[j][i]==player):
						countc+=1
				if(countr==3 or countc==3):
					return templist[t]
			if(tempboard[0][0]==player and tempboard[1][1]==player and tempboard[2][2]==player):
				return templist[t]
			if(tempboard[0][2]==player and tempboard[1][1]==player and tempboard[2][0]==player):
				return templist[t]

		return None #returning None if there is no winning move

	def threat_to_lose(self):
		# Run winning_move from other perspective
		temp=0 #storing player in temporary variable
		if(self.AITurn==1):
			temp=2
		else:
			temp=1
		return self.winning_move(temp) #checking if player can win in a next move so that AI can block that move accordingly

	def smart_move(self):
		if(self.winning_move(self.turn)!=None):
			self.make_move(self.winning_move(self.turn), self.AITurn) #if there is a winning move, making that move
			return
		elif(self.threat_to_lose()!=None):
			self.make_move(self.threat_to_lose(), self.AITurn) #blocking a threat in case there is any
			return
		self.make_move(self.make_random_move(), self.AITurn) #making random move 
		return

sim = TicTacToeSim() #creating instance of the game
sim.play_game() #calling driver function

