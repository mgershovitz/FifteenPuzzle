from common import consts
from game_logic import PuzzleGame

WINNING_BOARD = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, consts.EMPTY_STR]]
LOSING_BOARD = [[1, 2, 3],
                [4, 5, 6],
                [7, consts.EMPTY_STR, 8]]

class TestGameBoard(object):
    def __init__(self):
        self.tester = PuzzleGame()

    def test_get_new_randomized_board(self):
        pass

    def test_win(self):
        self.tester.board = WINNING_BOARD
        assert self.tester.win()

        self.tester.board = LOSING_BOARD
        assert not self.tester.win()
