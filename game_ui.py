import consts
from display_modules.basic_display import BasicDisplayUtils
from display_modules.controlled_display import ControlledDisplayUtils
from game_logic import PuzzleGame
from input_manager import InputManager
from settings import GameManager


class PuzzleGameUI(object):
    def __init__(self):
        self.game = PuzzleGame()
        self.settings = GameManager()
        self.display = BasicDisplayUtils()
        self.input_manager = InputManager()

    def settings_check(self):
        InputManager.user_input_loop(
            message=consts.EDIT_SETTINGS_PROMPT,
            valid_inputs=[consts.YES, consts.NO],
            input_to_action={'y': self.settings.handle_settings_edit}
        )

    def movement_settings(self):
        InputManager.user_input_loop(
            message=consts.EDIT_MOVEMENT_SETTINGS_PROMPT,
            valid_inputs=[consts.YES, consts.NO],
            input_to_action={'y': self.input_manager.get_movement_keys_edit_func(self.display.get_user_input)}
        )

    def init_new_game(self):
        print(consts.README)
        print(consts.INIT_NEW_BOARD)
        self.game.get_new_randomized_board(self.settings.board_size)
        print(consts.LETS_START_THE_GAME)

    def run(self):
        self.display.init_display()
        self.display.display_game_board(self.game.board)

        while True:
            key = self.display.get_user_input()
            user_move = self.input_manager.get_user_move(key)
            if user_move is None:
                break

            self.game.move(user_move)
            self.display.display_game_board(self.game.board)

        if isinstance(self.display, ControlledDisplayUtils):
            self.display.break_display_control()

    def gameplay(self):
        print(consts.GAME_OPENING)
        self.settings_check()
        self.movement_settings()
        self.init_new_game()
        self.run()


if __name__ == '__main__':
    PuzzleGameUI().gameplay()