import curses

from common.consts import TABLE_PADDING
from display_modules.basic_display import BasicDisplayUtils


class ControlledDisplayUtils(BasicDisplayUtils):
    def __init__(self):
        super(ControlledDisplayUtils, self).__init__()
        self.screen = None

    def init_display(self):
        self.init_display_control()

    def get_user_input(self):
        return self.screen.getch

    def display_message(self, message):
        self.screen.addstr(0, 0, message)

    def display_game_board(self, board):
        board_display_matrix = self.get_baord_display_matrix(board)
        for pos, val in board_display_matrix.items():
            self.screen.addstr(pos[0], pos[1], val)

    def init_display_control(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

    def break_display_control(self):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()

    @staticmethod
    def get_baord_display_matrix(board):
        board_display = {}
        board_size = len(board)
        for i in range(0, board_size):
            for j in range(0, board_size):
                position = (i, j*TABLE_PADDING)
                val = str(board[i][j])
                board_display[position] = val

        return board_display
