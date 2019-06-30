import unittest

from common import consts
from game_logic import PuzzleGame
from settings import SettingsManager

WINNING_BOARD = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, consts.EMPTY_STR]]
LOSING_BOARD = [[1, 2, 3],
                [4, 5, 6],
                [7, consts.EMPTY_STR, 8]]

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.tester = PuzzleGame()
        self.test_settings = SettingsManager()
        self.test_settings.load_settings()

    def test_game_won(self):
        self.tester.init_game(self.test_settings, WINNING_BOARD)
        assert self.tester.game_won()

        self.tester.init_game(self.test_settings, LOSING_BOARD)
        assert not self.tester.game_won()
