import consts
from board_utils import BoardPosition

class PuzzleGame(object):
    def __init__(self):
        self.board = None
        self.board_size = None
        self.empty_spot = BoardPosition(2, 2)

    def get_new_randomized_board(self, board_size):
        board = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, consts.EMPTY_STR]]
        self.board = board
        self.board_size = board_size

    def move(self, user_move):
        new_empty_spot = self.get_new_empty_spot_position(user_move)
        if new_empty_spot:
            old_empty_spot = self.empty_spot
            self.set(old_empty_spot, self.get(new_empty_spot))
            self.set(new_empty_spot, consts.EMPTY_STR)
            self.empty_spot = new_empty_spot

    def set(self, pos, val):
        self.board[pos.x][pos.y] = val

    def get(self, pos):
        return self.board[pos.x][pos.y]

    def check_valid_position(self, pos):
        return 0 <= pos.x <= self.board_size - 1 and 0<= pos.y <= self.board_size - 1

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

        if new_pos and self.check_valid_position(new_pos):
            return new_pos
