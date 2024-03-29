from common import consts
from common.basic_display import BasicDisplayUtils
from game_logic import PuzzleGame
from common.input_manager import InputManager
from menus import Menus
from settings.key_settings import KeySettingsManager
from settings.game_settings import GameSettingsManager


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
        self.menus = None

    def main_game_loop(self):
        while True:
            self.display.display_table(self.game.get_display_matrix())
            if self.game.game_won():
                self.handle_game_won()

            key = self.input_manager.get_user_input()
            user_move = self.input_manager.get_user_move(key)
            if user_move is None:
                if self.input_manager.basic_user_input_loop(
                        consts.SURE_YOU_WANT_TO_QUIT, [consts.YES, consts.NO]) == consts.YES:
                    self.menus.open_main_menu()

            if user_move:
                self.game.move(user_move)

    def handle_game_won(self):
        if self.input_manager.basic_user_input_loop(consts.WIN_MESSAGE, [consts.YES, consts.NO]) == consts.YES:
            self.start_new_game()
        else:
            self.quit()

    def start_new_game(self):
        print(consts.INIT_NEW_BOARD)
        self.game.generate_new_puzzle(self.game_settings)
        print(consts.LETS_START_THE_GAME)
        self.main_game_loop()

    def run(self):
        self.display.display_message(consts.GAME_OPENING)
        self.display.display_message(consts.RULES)
        self.menus.open_main_menu()

    @staticmethod
    def quit():
        print(consts.GOODBYE)
        exit(0)

    def bootstrap(self):
        self.game_settings.load_settings()
        self.keys_settings.load_settings()
        self.display = BasicDisplayUtils()
        self.input_manager = InputManager(self.keys_settings, self.display)
        self.menus = Menus(self.input_manager, self.display, self.game_settings, self.keys_settings,
                           self.start_new_game, self.quit)

def play_in_cli():
    game = PuzzleGameUI()
    game.bootstrap()
    game.run()


if __name__ == '__main__':
    play_in_cli()
