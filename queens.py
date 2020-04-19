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
        self.full = False

    def __str__(self):
        return NEWLINE.join([TAB.join(row) for row in self.board])

    def change(self, y, x):
        """
        Receives coordinates to change from empty to queen or from queen to empty
        """
        # x = column, 0 based, left to right
        # y = row, 0 based, top to bottom
        if self.board[y][x] == EMPTY:
            self.board[y][x] = QUEEN
        else:
            self.board[y][x] = EMPTY

    def mirrored(self):
        """
        """
        temp = Board()
        temp.board = [row[::-1] for row in self.board]
        return temp

    def flipped(self):
        """
        """
        temp = Board()
        temp.board = self.board[::-1]
        return temp

    def spin(self, times=1):
        """
        Spins board clockwise, default once
        """
        temp = Board()
        for time in range(times):
            for row in range(SIZE):
                for col in range(SIZE):
                    new_col = SIZE - 1 - row
                    new_row = col
                    temp.board[new_row][new_col] = self.board[row][col]
        return temp

    def update_used(self):
        """
        """
        board_list = [self, self.flipped(), self.mirrored(),
                        self.flipped().mirrored()]
        new_list = []
        for i in board_list:
            new_list.append(i.board)
            new_list.append(i.spin().board)
            new_list.append(i.spin(3).board)
        for i in new_list:
            print(i)

        self.used.append(new_list)


    def check_used(self):
        """
        Checks if solution is a permutation of a previously found solution
        """
        # print(self.used[0])
        print(self.board in self.used)


def main():
    b1 = Board()
    b1.change(1, 1)
    b1.change(0, 0)
    b1.change(1, 0)
    b1.change(4, 3)
    print(b1)
    # # b1.change(6, 6) 3) * '='
    # # print(b1, b1.mirrored(), b1.flipped(), b1.mirrored().flipped(),
    # #         b1.spin()
    # # sep = (4 * SIZE -, sep=f'\n{sep}\n', end='\n')
    # b1.update_used()
    # b1.check_used()
    # print(b1.board)
    # b1 = b1.flipped()
    # b1.check_used()
    # print(b1.board)
    # b1.change(3, 3)
    # b1.check_used()
    # print(b1.board)



if __name__ == '__main__':
    main()