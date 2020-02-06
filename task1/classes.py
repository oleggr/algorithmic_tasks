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
        '''
        Normal step of cell live.
        Time of step regulating in external system.
        '''

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

        # Create adapted mattrix from board.
        # From 
        #     a11 a12
        #     a21 a22

        # To
        #     a22 a21 a22 a21
        #     a12 a11 a12 a11
        #     a22 a21 a22 a21
        #     a12 a11 a12 a11

        tmp_board = []
        subarray = []

        subarray.append(self.board[y-1][x-1])
        subarray.extend(self.board[y-1])
        subarray.append(self.board[y-1][0])

        tmp_board.append(subarray)

        for line in self.board:

            subarray = []

            subarray.append(line[-1])
            subarray.extend(line)
            subarray.append(line[0])

            tmp_board.append(subarray)

        subarray = []

        subarray.append(self.board[0][x-1])
        subarray.extend(self.board[0])
        subarray.append(self.board[0][0])

        tmp_board.append(subarray)

        for j in range(y):
            for i in range(x):

                i1 = i + 1
                j1 = j + 1

                try:
                    self.neighbors_matrix[j][i] += tmp_board[j1-1][i1-1] \
                            + tmp_board[j1][i1-1] \
                            + tmp_board[j1+1][i1-1] \
                            + tmp_board[j1+1][i1] \
                            + tmp_board[j1+1][i1+1] \
                            + tmp_board[j1][i1+1] \
                            + tmp_board[j1-1][i1+1] \
                            + tmp_board[j1-1][i1]

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