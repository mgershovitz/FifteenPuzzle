from board_utils.board_generator import RandomBoardGenerator
from common import consts
from board_utils.matrix_board import BoardPosition

class PuzzleGame(object):
    def __init__(self):
        self.game_board = None
        self.random_board_generator = RandomBoardGenerator()

        self.tiles_in_place = None
        self.tiles_not_in_place = None

    def generate_new_puzzle(self, game_settings, fixed_board=None, fixed_empty_spot=None):
        if game_settings.get(consts.BOARD_SIZE_STR) != self.random_board_generator.board_size:
            self.random_board_generator.reset_board_size(game_settings.get(consts.BOARD_SIZE_STR))

        self.game_board = self.random_board_generator.generate_board(
            difficulty=game_settings.get(consts.DIFFICULTY_LEVEL_STR),
            fixed_board=fixed_board, fixed_empty_spot=fixed_empty_spot
        )
        self.create_initial_game_state()

    def game_won(self):
        return len(self.tiles_not_in_place) == 0

    def move(self, user_move):
        results = self.game_board.execute_move(user_move)
        if results:
            old_empty_spot, new_empty_spot = results
            self.update_game_state(old_empty_spot, new_empty_spot)

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
        self.tiles_in_place = set()
        self.tiles_not_in_place = set()

        for i in range(0, self.game_board.board_size):
            for j in range(0, self.game_board.board_size):
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
