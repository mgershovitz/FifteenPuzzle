from common import consts
from board_utils import BoardPosition

class PuzzleGame(object):
    def __init__(self):
        self.board = None
        self.board_size = None
        self.empty_spot = None

    def init_game(self, game_settings):
        self.empty_spot = BoardPosition.get_position_from_indexes_tuple(game_settings.get(consts.EMPTY_SPOT_STR))
        self.board_size = game_settings.get(consts.BOARD_SIZE_STR)
        self.get_new_randomized_board()

    def get_new_randomized_board(self):
        n = 1
        self.board = list()
        for i in range(0, self.board_size):
            self.board.append(list())
            for j in range(0, self.board_size):
                if self.empty_spot.x == i and self.empty_spot.y == j:
                    self.board[i].append(consts.EMPTY_STR)
                else:
                    self.board[i].append(n)
                    n += 1

    def move(self, user_move):
        new_empty_spot = self.get_new_empty_spot_position(user_move)
        if new_empty_spot:
            old_empty_spot = self.empty_spot
            self.set(old_empty_spot, self.get(new_empty_spot))
            self.set(new_empty_spot, consts.EMPTY_STR)
            self.empty_spot = new_empty_spot

    def win(self):
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if i == self.board_size - 1 and j == self.board_size - 1:
                    continue
                if self.board[i][j] != i*self.board_size + j + 1:
                    return False
        return True

    def set(self, pos, val):
        self.board[pos.x][pos.y] = val

    def get(self, pos):
        return self.board[pos.x][pos.y]

    def get_new_empty_spot_position(self, dir):
        # The empty spot is not the one that moves, the adjacent cells move,
        # So to make a right move, we need to check if the left adjacent cell can move right etc...
        new_pos = None
        if dir == consts.RIGHT:
            new_pos = self.empty_spot.get_adj_left()
        elif dir == consts.LEFT:
            new_pos = self.empty_spot.get_adj_right()
        elif dir == consts.UP:
            new_pos = self.empty_spot.get_adj_down()
        elif dir == consts.DOWN:
            new_pos = self.empty_spot.get_adj_up()

        if new_pos and new_pos.is_valid_board_position(self.board_size):
            return new_pos
