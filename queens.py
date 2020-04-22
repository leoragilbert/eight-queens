QUEEN = 'Q'
EMPTY = '•'
TAB = '\t'
NEWLINE = '\r\n'
SIZE = 8

class Board:
    def __init__(self, size=SIZE):
        self.size = size
        self.board = [[EMPTY for i in range(size)] for i in range(size)]

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
        temp = self
        if self.board[y][x] == EMPTY:
            temp.board[y][x] = QUEEN
        else:
            temp.board[y][x] = EMPTY
        return temp


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

        # self.used.extend(new_list)
        return new_list


    def check_used(self, used):
        """
        Checks if solution is a permutation of a previously found solution
        To be called if board is full and is a viable solution.
        :param used: list of boards
        :return: True if board is a permutation of a previously found solution.
        False if not (if it's a new solution)
        """
        return self.board in used


    def check_solved(self):
        """
        Checks if board is solved
        :return: bool
        """
        for row in self.board:
            if QUEEN not in row:
                return False
        return True


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
    for i in range(x - board.size, x + board.size + 1):
        for j in range(y - board.size, y + board.size + 1):
            if i >= 0 and j >= 0 and abs(i - x) == abs(j - y) or \
               i == x or j == y:
                try:
                    results.append(board.board[j][i] == QUEEN)
                except:
                    pass
    return True not in results

def find_solutions(board, row=0, found=0, used=[]):
    """
    Recursively finds all possible solutions to 8 queens problem.
    :param board: Board
    :param found: amount of solutions that have been found
    :param used: used boards
    :param row: current row
    :return: number of found solutions
    """


def main():
    b1 = Board()
    find_solutions(b1)
    # print(b1.solutions)


if __name__ == '__main__':
    main()