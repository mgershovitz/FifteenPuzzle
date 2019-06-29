from board_utils import GameBoard
from settings import GameSettings


class PuzzleGame(object):
    def __init__(self):
        self.board = None
        self.settings = GameSettings()

    def init_board(self):
        self.board = GameBoard.get_new_randomized_board(self.settings.board_size)

    def edit_settings(self):
        print(self.settings)
        self.handle_user_input(self.settings.get_edit_message(),
                               self.settings.get_valid_inputs_for_editing(),
                               self.settings.get_settings_number_to_edit_action())

    def handle_user_input(self, message, valid_inputs, input_to_action):
        user_input = None
        while user_input not in valid_inputs:
            print(message)
            user_input = input()

        if user_input in input_to_action:
            input_to_action[user_input]()