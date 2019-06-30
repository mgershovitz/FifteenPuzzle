import copy

from board_utils.matrix_board import BoardPosition, Board
from common import consts
import random

class RandomBoardGenerator(object):
    def __init__(self, board_size, empty_spot):
        self.game_board = None

        self.board_size = board_size
        self.initial_empty_spot = BoardPosition.get_position_from_indexes_tuple(empty_spot)
        self.solved_board = self.get_solved_board()

    def get_solved_board(self):
        n = 1
        board = list()
        for i in range(0, self.board_size):
            board.append(list())
            for j in range(0, self.board_size):
                if self.initial_empty_spot.x == i and self.initial_empty_spot.y == j:
                    board[i].append(consts.EMPTY_STR)
                else:
                    board[i].append(n)
                    n += 1
        return board

    def generate_board(self, difficulty, fixed_board=None):
        self.game_board = Board(
            copy.deepcopy(self.solved_board),
            self.board_size,
            self.initial_empty_spot
        )

        if fixed_board:
            self.game_board.board = fixed_board
        else:
            for i in range(0, 10*difficulty):
                self.move_randomly()

        return self.game_board

    def move_randomly(self):
        optional_moves = [
            pos for pos in self.game_board.empty_spot.get_all_neighbours() if self.game_board.is_valid_board_position(pos)
        ]
        chosen_move = random.choice(optional_moves)
        self.game_board.move_empty_spot_to_new_position(chosen_move)
