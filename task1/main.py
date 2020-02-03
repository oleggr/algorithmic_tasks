from classes import *


def print_matrix(matrix):

    y = len(matrix)
    x = len(matrix[0])

    for j in range(y):
        
        print('|', end=' ')
        
        for i in range(x):
            print(matrix[j][i], end=' ')
        
        print('|')


if __name__=='__main__':
    M = 3
    N = 3

    board_1 = Board(M, N)


    dataset = board_1.get_data()

    print_matrix(dataset.get('board'))
