from classes import *

M = 3
N = 2

board_1 = Board(M, N)

board_1.board_init()
board_1.build_neighbours_matrix()

dataset = board_1.get_data()

print(dataset)