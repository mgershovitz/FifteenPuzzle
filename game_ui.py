from common import consts
from display_modules.basic_display import BasicDisplayUtils
from display_modules.controlled_display import ControlledDisplayUtils
from game_logic import PuzzleGame
from input_manager import InputManager
from settings import GameSettingsManager, KeySettingsManager


class PuzzleGameUI(object):
    """
    Puzzle game user interface -
    Handles user interaction, run main game loop, calls display and logic modules.

    """
    def __init__(self):
        self.game = PuzzleGame()
        self.game_settings = GameSettingsManager()
        self.keys_settings = KeySettingsManager()
        self.input_manager = None
        self.display = None

    def init_new_game(self):
        print(consts.README)
        print(consts.INIT_NEW_BOARD)

        self.game.init_new_puzzle()
        print(consts.LETS_START_THE_GAME)

    def main_game_loop(self):
        self.display.init_display()

        while True:
            self.display.display_table(self.game.get_display_matrix())
            if self.game.game_won():
                self.input_manager.basic_user_input_loop(consts.WIN_MESSAGE, [consts.YES, consts.NO],
                                                         {'y': self.start_new_game,
                                                          'n': self.quit})

            key = self.display.get_user_input()
            user_move = self.input_manager.get_user_move(key)
            if user_move is None:
                self.input_manager.basic_user_input_loop(consts.SURE_YOU_WANT_TO_QUIT, [consts.YES, consts.NO],
                                                         {'y': self.quit})

            if user_move:
                self.game.move(user_move)

    def start_new_game(self):
        self.init_new_game()
        self.main_game_loop()

    def quit(self):
        if isinstance(self.display, ControlledDisplayUtils):
            self.display.break_display_control()

        print(consts.GOODBYE)
        exit(0)

    def run(self):
        self.display.display_message(consts.GAME_OPENING)
        self.input_manager.edit_game_settings()
        self.input_manager.edit_keys_settings()

        self.game.init_game(self.game_settings)

        self.start_new_game()

    def bootstrap(self):
        self.game_settings.load_settings()
        self.display = BasicDisplayUtils() if self.game_settings.get(consts.DISPLAY_TYPE_STR) == consts.BASIC_DISPLAY_TYPE \
            else ControlledDisplayUtils()
        self.input_manager = InputManager(self.game_settings, self.keys_settings, self.display)


if __name__ == '__main__':
    game = PuzzleGameUI()
    game.bootstrap()
    game.run()
