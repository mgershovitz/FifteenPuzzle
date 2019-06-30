import consts
from display_modules.basic_display import BasicDisplayUtils
from display_modules.controlled_display import ControlledDisplayUtils
from game_logic import PuzzleGame
from input_manager import InputManager
from settings import SettingsManager


class PuzzleGameUI(object):
    """
    Puzzle game user interface -
    Handles user interaction, run main game loop, calls display and logic modules.

    """

    def __init__(self):
        self.game = PuzzleGame()
        self.settings = SettingsManager()
        self.input_manager = None
        self.display = None

    def movement_settings(self):
        InputManager.user_input_loop(
            message=consts.EDIT_MOVEMENT_SETTINGS_PROMPT,
            valid_inputs=[consts.YES, consts.NO],
            input_to_action={'y': self.input_manager.get_movement_keys_edit_func(self.display.get_user_input)}
        )

    def init_new_game(self):
        print(consts.README)
        print(consts.INIT_NEW_BOARD)
        self.game.init_game(self.settings)
        print(consts.LETS_START_THE_GAME)

    def start(self):
        self.display.init_display()
        self.display.display_game_board(self.game.board)

        while True:
            if self.game.win():
                self.input_manager.user_input_loop(consts.WIN_MESSAGE,
                                                   [consts.YES, consts.NO],
                                                   {'y': self.init_new_game_and_start,
                                                    'n': self.quit})

            key = self.display.get_user_input()
            user_move = self.input_manager.get_user_move(key)
            if user_move is None:
                break

            self.game.move(user_move)
            self.display.display_game_board(self.game.board)

        if isinstance(self.display, ControlledDisplayUtils):
            self.display.break_display_control()

    def init_new_game_and_start(self):
        self.init_new_game()
        self.start()

    def quit(self):
        print(consts.GOODBYE)
        exit(0)

    def run(self):
        print(consts.GAME_OPENING)
        self.input_manager.edit_settings()
        self.movement_settings()
        self.init_new_game_and_start()

    def bootstrap(self):
        self.settings.load_settings()
        self.display = BasicDisplayUtils() if self.settings.get(consts.DISPLAY_TYPE_STR) == consts.DEFAULT_DISPLAY_TYPE \
            else ControlledDisplayUtils()
        self.input_manager = InputManager(self.settings, self.display)


if __name__ == '__main__':
    game = PuzzleGameUI()
    game.bootstrap()
    game.run()
