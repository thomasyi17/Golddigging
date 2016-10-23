#Vignesh Ramchandran, Thomas Yi, Rajiv Deshpande
#goldigging cdw
import random
import numpy as np

def print_matrix(matrix):
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			print matrix[i,j],
		print("")

def main():

	print("""Welcome to Golddigging CDW: Coding Done Wrong. This will be the most interesting game you ever play in your life. The only rules are to follow what we say.
	The goal of the game is to find treasure. You will be presented with a grid that will tell you 3 important things.
		1. It will tell you where you are: '*'
		2. It will tell you what locations are safe: 'C'
		3. It will tell you how many mines are adjacent to you at your current location.
	Other than that, it is up to you to find a safe path to the treasure, or get rekt along the way. 
	Note, you can indeed spawn on treasure because life can be nice like that. 
	Also, it is possible to just straight up not be able to move anywhere because you are surroudned by mines. Life isn't always nice.
	\n\n
	 """)

	board_width = input("Enter the board width you want to play with:")
	board_height = input("Enter the board width you want to play with:")
	if board_width <= 0 or board_height <= 0:
		print("You think you're so smart?")
		return

	matrix = np.zeros((board_width, board_height),dtype="str")
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			matrix[i,j] = "X"	

	pp_col = random.randint(0,board_width-1)
	pp_row = random.randint(0,board_height-1)

	matrix[pp_row,pp_col] = "*"

	matrix_mines = np.zeros((board_width, board_height),dtype = int)
	for row in range(matrix_mines.shape[0]):
		for col in range(matrix_mines.shape[1]):
			rand = random.randint(0,2)
			if rand == 2:
				matrix_mines[row,col] = 1

	matrix_mines[pp_row, pp_col] = 0
	treasure_col = random.randint(0,board_width-1)
	treasure_row = random.randint(0,board_height-1)
	matrix_mines[treasure_row, treasure_col] = 0

	while True:
		print_matrix(matrix)
		steps_away = abs(pp_row - treasure_row) + abs(pp_col - treasure_col)
		print("You are {} steps away from the treasure".format(steps_away))

		if pp_row == treasure_row and pp_col == treasure_col:
			print("Congrats! You Win! You found yoself some treasurz")
			break

		curr_col = pp_col
		curr_row = pp_row
		num_mines = 0
		if matrix_mines[curr_row,(curr_col+board_width+1)%board_width] == 1:
			num_mines += 1
		if matrix_mines[curr_row,(curr_col+board_width-1)%board_width] == 1:
			num_mines += 1
		if matrix_mines[(curr_row + board_height + 1)%board_height, curr_col] ==1:
			num_mines += 1
		if matrix_mines[(curr_row + board_height - 1)%board_height, curr_col] == 1:
			num_mines += 1

		print("You have {} mine(s) next to you\n".format(num_mines))
		direction = raw_input("Enter (u)p, (d)own, (l)eft, (r)ight: ")

		if direction == "u":
			pp_row -= 1
		elif direction == "d":
			pp_row += 1
		elif direction == "r":
			pp_col += 1
		elif direction == "l":
			pp_col -= 1
		else:
			print("You done goofed. Enter a real direction.")


		pp_row = (pp_row + board_height)%board_height
		pp_col = (pp_col + board_width)%board_width

		if matrix_mines[pp_row, pp_col] == 1:
			matrix[treasure_row, treasure_col] = "T"
			print("you got rekt!")
			print("Treasure location: ")
			print_matrix(matrix)
			print("")
			print("Mine locations: ")
			print_matrix(matrix_mines)
			print("Treasure and mine locations")
			break


		matrix[curr_row,curr_col] = "C"
		matrix[pp_row,pp_col] = "*"


main()