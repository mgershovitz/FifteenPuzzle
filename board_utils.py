from texttable import Texttable

class GameBoard(object):
    def __init__(self, board=None, board_size=None):
        self.board = board
        self.size = board_size

    def __repr__(self):
        t = Texttable()
        for i in range(0, self.size):
            t.add_row(self.board[i])
        return t.draw()

    @classmethod
    def get_new_randomized_board(cls, board_size):
        board = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, '']]
        return GameBoard(board, board_size)
