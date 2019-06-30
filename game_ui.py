from common import consts
from display_modules.basic_display import BasicDisplayUtils
from game_logic import PuzzleGame
from input_manager import InputManager
from settings.settings import GameSettingsManager, KeySettingsManager


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
                user_quit = self.input_manager.basic_user_input_loop(consts.SURE_YOU_WANT_TO_QUIT, [consts.YES, consts.NO])
                if user_quit == 'y':
                    self.menu()

            if user_move:
                self.game.move(user_move)

    def quit(self):
        print(consts.GOODBYE)
        exit(0)

    def start_new_game(self):
        print(consts.INIT_NEW_BOARD)
        self.game.generate_new_puzzle()
        print(consts.LETS_START_THE_GAME)

        self.main_game_loop()

    def menu(self):
        self.input_manager.basic_user_input_loop(consts.MENU_OPTIONS,
                                                 ['1', '2', '3', '4'],
                                                 {'1': self.input_manager.handle_game_settings_edit,
                                                  '2': self.input_manager.handle_keys_settings_edit,
                                                  '3': self.start_new_game,
                                                  '4': self.quit})
        self.menu()

    def run(self):
        self.game.init_game(self.game_settings)
        self.display.display_message(consts.GAME_OPENING)
        self.display.display_message(consts.RULES)

        self.menu()

    def bootstrap(self):
        self.game_settings.load_settings()
        self.keys_settings.load_settings()
        self.display = BasicDisplayUtils()
        self.display.init_display()
        self.input_manager = InputManager(self.game_settings, self.keys_settings, self.display)


if __name__ == '__main__':
    game = PuzzleGameUI()
    game.bootstrap()
    game.run()
