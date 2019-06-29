import consts
from game_logic import PuzzleGame

class PuzzleGameUI(object):
    def __init__(self):
        self.game = PuzzleGame()

    def settings_check(self):
        self.game.handle_user_input(
            message=consts.EDIT_SETTINGS_PROMPT,
            valid_inputs=[consts.YES, consts.NO],
            input_to_action={'y': self.game.edit_settings}
        )

    def init_new_game(self):
        print(consts.INIT_NEW_BOARD)
        self.game.init_board()
        print(self.game.board)

    def gameplay(self):
        print(consts.GAME_OPENING)
        self.settings_check()
        self.init_new_game()


if __name__ == '__main__':
    PuzzleGameUI().gameplay()