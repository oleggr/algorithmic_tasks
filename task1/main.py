'''
Task1

Usage: python3 main.py

Github: github.com/oleggr/internship_preparation
'''


import os
import time
from classes import *


__author__ = 'oleggr'
__email__ = 'oleg.gr@outlook.com'


def print_matrix(matrix):
    '''
    Print func for matrix

    :param matrix: list - matrix to print
    '''

    y = len(matrix)
    x = len(matrix[0])

    for j in range(y):
        
        print('|', end=' ')
        
        for i in range(x):
            print(matrix[j][i], end=' ')
        
        print('|')


if __name__=='__main__':
    
    # Time of 1 single step in seconds
    step_time = 1
    step_counter = 0

    # Name of file with board
    filename = 'board.txt'

    # Create board object    
    board_1 = Board()

    # Show startup menu
    os.system('cls')
    choise = input('0 for random generation\n1 board from file\n')

    # Choose configuration method
    if choise == '0':
        M = int(input('Num of columns:'))
        N = int(input('Num of lines:'))
        board_1.init_board(M, N)

    elif choise == '1':
        board_1.init_board_from_file(filename)

    else:
        print('wrong input')
        input()
        raise SystemExit

    # Main cycle
    while True:

        # Show data
        os.system('cls')
        print_matrix(board_1.get_board())
        print('\nstep count: {}'.format(step_counter))

        # Make a step of the system
        board_1.live_step()
        step_counter += 1

        # Wait step time
        time.sleep(step_time)
