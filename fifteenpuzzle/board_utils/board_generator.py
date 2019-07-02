import copy
import random

from fifteenpuzzle.board_utils.matrix_board import BoardPosition, Board
from fifteenpuzzle.common import consts


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
                self.move_randomly(board)

        return board

    @classmethod
    def move_randomly(cls, board):
        optional_moves = [
            pos for pos in board.empty_spot.get_all_neighbours() if board.is_valid_board_position(pos)
        ]
        chosen_move = random.choice(optional_moves)
        board.move_empty_spot_to_new_position(chosen_move)
