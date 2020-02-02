import random


class Board():
    '''
    Class of the board. 
    Description of the size of the board
    and properties of the cells.
    ''' 


    # TODO: Implement board generation by percent of live cells
    # percent_of_live_cells = 5


    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y


    def board_init(self):
        # num_of_1 = int(round(self.size_x \
        #     * self.size_y \
        #     * (self.percent_of_live_cells / 100)))

        random.seed(3)
        self.board = [[random.randint(0,1) for e in range(self.size_x)] for e in range(self.size_y)]


    def build_neighbours_matrix(self):
        self.neighbours_matrix = [[0 for e in range(self.size_x)] for e in range(self.size_y)]

        for j in range(self.size_y):
            for i in range(self.size_x):
                self.neighbours_matrix[j][i] = 2


    def get_data(self):

        dataset = {
        'board': self.board,
        'nghbr_mtrx': self.neighbours_matrix,
        'size_x': self.size_x,
        'size_y': self.size_y
        }

        return dataset


    # Rules to check
    def live_cell_lives(self, num_of_neighbours):
        if (num_of_neighbours < 2) or (num_of_neighbours > 3):
            return False
        return True


    def dead_cell_reborn(self, num_of_neighbours):
        if (num_of_neighbours == 3):
            return True
        return False


    def __repr__(self):
        self_oject = {
                'size_x': self.size_x,
                'size_y': self.size_y
        }
        return str(self_oject)