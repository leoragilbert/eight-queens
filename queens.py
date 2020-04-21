QUEEN = 'Q'
EMPTY = '•'
TAB = '\t'
NEWLINE = '\r\n'
SIZE = 8

class Board:
    def __init__(self, size=SIZE):
        self.size = size
        self.board = [[EMPTY for i in range(size)] for i in range(size)]
        self.used = []
        self.solved = False
        self.solutions = 0

    def __str__(self):
        return NEWLINE.join([TAB.join(row) for row in self.board])

    def change(self, y, x):
        """
        Receives coordinates to change from empty to queen or from queen to empty
        :param y: y coordinate
        :param x: x coordinate
        :return: None
        """
        # x = column, 0 based, left to right
        # y = row, 0 based, top to bottom
        if self.board[y][x] == EMPTY:
            self.board[y][x] = QUEEN
        else:
            self.board[y][x] = EMPTY

    def mirrored(self):
        """
        Returns Board with mirrored board
        :return: Board
        """
        temp = Board()
        temp.board = [row[::-1] for row in self.board]
        return temp


    def spin(self):
        """
        Returns list of boards created by spinning current board 3 times.
        :return: list of boards
        """
        temp = Board()
        copy = self
        board_list = []
        for time in range(3):
            for row in range(SIZE):
                for col in range(SIZE):
                    new_col = SIZE - 1 - row
                    new_row = col
                    temp.board[new_row][new_col] = copy.board[row][col]
            copy = temp
            board_list.append(temp.board)
            temp = Board()
        return board_list


    def update_used(self):
        """
        Updates boards used parameter with a new solution and its permutations.
        :return: None
        """
        board_list = [self, self.mirrored()]
        new_list = []
        for i in board_list:
            new_list.append(i.board)
            new_list.extend(i.spin())

        self.used.extend(new_list)


    def check_used(self):
        """
        Checks if solution is a permutation of a previously found solution
        To be called if board is full and is a viable solution.
        :return: True if board is a permutation of a previously found solution.
        False if not (if it's a new solution)
        """
        return self.board in self.used


def is_safe(board, y, x):
    """
    Receives a board and coordinates, checks if the coordinates are a safe
    place for a new queen
    :param board: Board
    :param y: y coordinate
    :param : x coordinate
    :return: bool (True if the point is safe)
    """
    results = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i > 0 and j > 0:
                try:
                    results.append(board.board[j][i] == QUEEN)
                except:
                    pass
    return True not in results

def find_solutions(board, prev_y=0, prev_x=0):
    """
    Recursively finds all possible solutions to 8 queens problem.
    :param board: Board
    :param prev_y: y coordinate of the last queen to be placed
    # not sure if is relevant, seems redundant
    :param prev_x: x coordinate of previous queen
    """

def main():
    b1 = Board()
    b1.change(1, 1)
    b1.change(0, 0)
    b1.change(1, 0)
    b1.change(4, 3)
    print(b1)


if __name__ == '__main__':
    main()