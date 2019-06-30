from board_utils.board_generator import RandomBoardGenerator
from common import consts
from board_utils.matrix_board import Board, BoardPosition


class PuzzleGame(object):
    def __init__(self):
        self.game_board = None
        self.board_size = None

        self.tiles_in_place = set()
        self.tiles_not_in_place = set()

        self.board_generator = RandomBoardGenerator(self.board_size)

    def init_game(self, game_settings, fixed_board=None):
        self.board_size = game_settings.get(consts.BOARD_SIZE_STR)
        empty_spot = game_settings.get(consts.EMPTY_SPOT_STR)
        if fixed_board:
            board = fixed_board
        else:
            board = self.board_generator.generate_board(empty_spot)

        self.game_board = Board(board, self.board_size, empty_spot)
        self.create_initial_game_state()

    def game_won(self):
        return len(self.tiles_not_in_place) == 0

    def move(self, user_move):
        old_empty_spot, new_empty_spot = self.game_board.execute_move(user_move)
        if new_empty_spot:
            self.update_game_state(old_empty_spot, new_empty_spot)
        print(self.tiles_not_in_place)

    def update_game_state(self, old_empty_spot, new_empty_spot):
        if new_empty_spot in self.tiles_not_in_place:
            self.tiles_not_in_place.remove(new_empty_spot)
        else:
            self.tiles_in_place.remove(new_empty_spot)

        if self.game_board.position_matches_value(old_empty_spot):
            self.tiles_in_place.add(old_empty_spot)
        else:
            self.tiles_not_in_place.add(old_empty_spot)

    def create_initial_game_state(self):
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                pos = BoardPosition(i, j)
                if self.game_board.get(pos) == consts.EMPTY_STR:
                    continue
                else:
                    if self.game_board.position_matches_value(pos):
                        self.tiles_in_place.add(pos)
                    else:
                        self.tiles_not_in_place.add(pos)

    def get_display_matrix(self):
        return self.game_board.board
