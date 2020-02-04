import os
import time
from classes import *


def print_matrix(matrix):

    y = len(matrix)
    x = len(matrix[0])

    for j in range(y):
        
        print('|', end=' ')
        
        for i in range(x):
            print(matrix[j][i], end=' ')
        
        print('|')


def print_board(board, neighbors_matrix):

    y = len(board)
    x = len(board[0])

    for j in range(y):
        
        print('|', end=' ')
        
        for i in range(x):
            print(board[j][i], end=' ')
        
        print('|', end=' ')

        for i in range(x):
            print(neighbors_matrix[j][i], end=' ')
        
        print('|')


if __name__=='__main__':
    
    M = 5 # num of columns
    N = 4 # num of lines

    filename = 'board.txt'
    step_counter = 0
    step_time = 1 # in sec

    board_1 = Board(M, N)

    os.system('cls')
    choise = input('0 for random generation\n1 board from file')

    if choise == '0':
        board_1.init_board()
    elif choise == '1':
        board_1.init_board_from_file(filename)
    else:
        print('wrong input\nrandom generation will be applied')
        input()
        board_1.init_board()

    board_1.build_neighbors_matrix()
    dataset = board_1.get_data()

    os.system('cls')
    print_board(dataset.get('board'), dataset.get('neighbors_matrix'))
    print('\nstep count: {}'.format(step_counter))

    time.sleep(step_time)

    # main cycle
    while True:

        os.system('cls')

        board_1.live_step()
        dataset = board_1.get_data()

        step_counter += 1

        print_board(dataset.get('board'), dataset.get('neighbors_matrix'))
        print('\nstep count: {}'.format(step_counter))

        time.sleep(step_time)
