import random


class Board():
    '''
    Class of the board. 
    Description of the size of the board
    and properties of the cells.
    '''


    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


    def init_board(self):
        random.seed(3)
        self.board = [[random.randint(0,1) for e in range(self.size_x)] for e in range(self.size_y)]


    def init_board_from_file(self, filename):

        self.board = []
        
        try:
            with open(filename, 'r') as f:
                for line in f:
                    subarray = []

                    for symbol in line:
                        if (symbol != '\n') and (symbol != ' '):
                            subarray.append(int(symbol))

                    self.board.append(subarray)

        except Exception as e:
            print(e)
            self.init_board()


    def live_step(self):

        y = self.size_y
        x = self.size_x

        self.build_neighbors_matrix()

        for j in range(y):
            for i in range(x):
                
                # if cell is alive
                if self.board[j][i]:
                    if not self.live_cell_lives(self.neighbors_matrix[j][i]):
                        self.board[j][i] = 0

                else:
                    if self.dead_cell_reborn(self.neighbors_matrix[j][i]):
                        self.board[j][i] = 1


    def build_neighbors_matrix(self):

        y = self.size_y
        x = self.size_x

        self.neighbors_matrix = [[0 for e in range(x)] for e in range(y)]

        for j in range(y):
            for i in range(x):

                try:

                    # 1 0 0
                    # 0 0 0
                    # 0 0 0
                    if (i == j == 0):
                        self.neighbors_matrix[j][i] += self.board[y - 1][x - 1] \
                                + self.board[j][x-1] \
                                + self.board[j+1][x-1] \
                                + self.board[j+1][i] \
                                + self.board[j+1][i+1] \
                                + self.board[j][i+1] \
                                + self.board[y-1][i+1] \
                                + self.board[y-1][i]

                    # 0 0 0
                    # 1 0 0
                    # 0 0 0
                    if (i == 0) and (0 < j < y - 1):
                        self.neighbors_matrix[j][i] += self.board[j-1][x-1] \
                                + self.board[j][x-1] \
                                + self.board[j+1][x-1] \
                                + self.board[j+1][i] \
                                + self.board[j+1][i+1] \
                                + self.board[j][i+1] \
                                + self.board[j-1][i+1] \
                                + self.board[j-1][i]

                    # 0 0 0
                    # 0 0 0
                    # 1 0 0
                    if (i == 0) and (j == y - 1):
                        self.neighbors_matrix[j][i] += self.board[j - 1][x - 1] \
                                + self.board[j][x-1] \
                                + self.board[0][x-1] \
                                + self.board[0][i] \
                                + self.board[0][i+1] \
                                + self.board[j][i+1] \
                                + self.board[j-1][i+1] \
                                + self.board[j-1][i]

                    # 0 0 0
                    # 0 0 0
                    # 0 1 0
                    if (0 < i < x - 1) and (j == y - 1):
                        self.neighbors_matrix[j][i] += self.board[j-1][i-1] \
                                + self.board[j][i-1] \
                                + self.board[0][i-1] \
                                + self.board[0][i] \
                                + self.board[0][i+1] \
                                + self.board[j][i+1] \
                                + self.board[j-1][i+1] \
                                + self.board[j-1][i]

                    # 0 0 0
                    # 0 0 0
                    # 0 0 1
                    if (i == x - 1) and (j == y - 1):
                        self.neighbors_matrix[j][i] += self.board[j-1][i-1] \
                                + self.board[j][i-1] \
                                + self.board[0][i-1] \
                                + self.board[0][i] \
                                + self.board[0][0] \
                                + self.board[j][0] \
                                + self.board[j-1][0] \
                                + self.board[j-1][i]

                    # 0 0 0
                    # 0 0 1
                    # 0 0 0
                    if (i == x - 1) and (0 < j < y - 1):
                        self.neighbors_matrix[j][i] += self.board[j-1][i-1] \
                                + self.board[j][i-1] \
                                + self.board[j+1][i-1] \
                                + self.board[j+1][i] \
                                + self.board[j+1][0] \
                                + self.board[j][0] \
                                + self.board[j-1][0] \
                                + self.board[j-1][i]

                    # 0 0 1
                    # 0 0 0
                    # 0 0 0
                    if (i == x - 1) and (j == 0):
                        self.neighbors_matrix[j][i] += self.board[y-1][i-1] \
                                + self.board[j][i-1] \
                                + self.board[j+1][i-1] \
                                + self.board[j+1][i] \
                                + self.board[j+1][0] \
                                + self.board[j][0] \
                                + self.board[y-1][0] \
                                + self.board[y-1][i]

                    # 0 1 0
                    # 0 0 0
                    # 0 0 0
                    if (0 < i < x - 1) and (j == 0):
                        self.neighbors_matrix[j][i] += self.board[y-1][i-1] \
                                + self.board[j][i-1] \
                                + self.board[j+1][i-1] \
                                + self.board[j+1][i] \
                                + self.board[j+1][i+1] \
                                + self.board[j][i+1] \
                                + self.board[y-1][i+1] \
                                + self.board[y-1][i]

                    # 0 0 0
                    # 0 1 0
                    # 0 0 0
                    if (0 < i < x - 1) and (0 < j < y - 1):
                        self.neighbors_matrix[j][i] += self.board[j-1][i-1] \
                                + self.board[j][i-1] \
                                + self.board[j+1][i-1] \
                                + self.board[j+1][i] \
                                + self.board[j+1][i+1] \
                                + self.board[j][i+1] \
                                + self.board[j-1][i+1] \
                                + self.board[j-1][i]

                except Exception as e:
                    print(e)


    def get_data(self):

        dataset = {
        'board': self.board,
        'neighbors_matrix': self.neighbors_matrix,
        'size_x': self.size_x,
        'size_y': self.size_y
        }

        return dataset


    # Rules to check
    def live_cell_lives(self, num_of_neighbors):
        if (num_of_neighbors < 2) or (num_of_neighbors > 3):
            return False
        return True


    def dead_cell_reborn(self, num_of_neighbors):
        if (num_of_neighbors == 3):
            return True
        return False


    def __repr__(self):
        self_oject = {
                'size_x': self.size_x,
                'size_y': self.size_y
        }
        return str(self_oject)