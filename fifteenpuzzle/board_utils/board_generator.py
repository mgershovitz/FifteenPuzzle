import copy

from board_utils.matrix_board import BoardPosition, Board
from common import consts


class RandomBoardGenerator(object):
    def __init__(self, board_size):
        self.board_size = board_size
        self.empty_spot = BoardPosition(self.board_size-1, self.board_size-1)
        self.solved_board = self.get_solved_board()

    def get_solved_board(self):
        n = 1
        board = list()
        for i in range(0, self.board_size):
            board.append(list())
            for j in range(0, self.board_size):
                if self.empty_spot.x == i and self.empty_spot.y == j:
                    board[i].append(consts.EMPTY_STR)
                else:
                    board[i].append(n)
                    n += 1
        return board

    def generate_board(self, difficulty, fixed_board=None):
        if fixed_board:
            board = Board(
                copy.deepcopy(fixed_board),
                len(fixed_board),
                self.empty_spot
            )
        else:
            board = Board(
                copy.deepcopy(self.solved_board),
                self.board_size,
                self.empty_spot
            )
            for i in range(0, 5*difficulty):
                self.execute_random_inversion(board)
                self.execute_random_inversion(board)

        return board

    def execute_random_inversion(self, board):
        # select 2 random positions

        first_pos = BoardPosition.get_random_pos(self.board_size)
        while first_pos == self.empty_spot:
            first_pos = BoardPosition.get_random_pos(self.board_size)

        second_pos = BoardPosition.get_random_pos(self.board_size)
        while second_pos == first_pos or second_pos == self.empty_spot:
            second_pos = BoardPosition.get_random_pos(self.board_size)

        tmp = board.get(first_pos)
        board.set(first_pos, board.get(second_pos))
        board.set(second_pos, tmp)
