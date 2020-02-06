import random


class Board():
    '''
    Class of the board. 
    Description of the size of the board
    and properties of the cells.
    '''     


    _random_seed = 3


    def init_board(self, size_x, size_y):
        '''
        Random board generation.

        :param size_x: int - number of columns in matrix
        :param size_y: int - number of lines in matrix
        '''

        self.size_x = size_x
        self.size_y = size_y

        random.seed(_random_seed)
        self.board = [[random.randint(0,1) for e in range(self.size_x)] for e in range(self.size_y)]

        self.build_neighbors_matrix()


    def init_board_from_file(self, filename):
        '''
        Board from file configuration.

        :param filename: str - name of file with configuration
        '''

        x = 0
        n = 0

        self.board = []
        
        try:
            with open(filename, 'r') as f:
                for line in f:
                    subarray = []

                    # Count num of elements in line
                    if x == 0:
                        x = line.count('0') + line.count('1') 

                    for symbol in line:
                        if (symbol != '\n') and (symbol != ' '):
                            subarray.append(int(symbol))
                            n += 1

                    self.board.append(subarray)

            self.size_x = x
            self.size_y = int(n / x)

        except Exception as e:
            print(e)
            raise SystemExit

        self.build_neighbors_matrix()


    def live_step(self):
        '''
        Normal step of cell live.
        Time of step regulating in external system.
        '''

        self.build_neighbors_matrix()

        for j in range(self.size_y):
            for i in range(self.size_x):
                
                # if cell is alive
                if self.board[j][i]:
                    if not self.live_cell_lives(self.neighbors_matrix[j][i]):
                        self.board[j][i] = 0

                else:
                    if self.dead_cell_reborn(self.neighbors_matrix[j][i]):
                        self.board[j][i] = 1


    def build_neighbors_matrix(self):
        '''
        Build matrix of neighbors for the board.
        Size of this matrix is the same as the board size.
        Each cell have value of number of neighbors in 
        the same cell number on the board.
        '''

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


    def get_board(self):
        return self.board


    def live_cell_lives(self, num_of_neighbors):
        '''
        Check if live cell is in good condition 
        and will live next step.

        :param num_of_neighbors: int - number of cell's neighbors
        '''

        if (num_of_neighbors < 2) or (num_of_neighbors > 3):
            return False
        return True


    def dead_cell_reborn(self, num_of_neighbors):
        '''
        Check if dead cell is in good condition 
        to reborn.

        :param num_of_neighbors: int - number of cell's neighbors
        '''

        if (num_of_neighbors == 3):
            return True
        return False


    def __repr__(self):
        '''
        Representation rules for Board class
        '''

        self_oject = {
                'size_x': self.size_x,
                'size_y': self.size_y
        }
        return str(self_oject)