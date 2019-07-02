import copy
import unittest

from board_utils.matrix_board import BoardPosition
from common import consts
from game_logic import PuzzleGame
from settings.game_settings import GameSettingsManager
from settings.settings import SettingsType

COMPLETED_BOARD = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, consts.EMPTY_STR]]
ALMOST_COMPLETED_BOARD = [[1, 2, 3],
                          [4, 5, 6],
                          [7, consts.EMPTY_STR, 8]]


def get_completed_board():
    return copy.deepcopy(COMPLETED_BOARD)


def get_almost_complete_board():
    return copy.deepcopy(ALMOST_COMPLETED_BOARD)


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.tester = PuzzleGame()
        self.test_settings = GameSettingsManager()
        self.test_settings.load_settings()
        self.test_settings.set(consts.BOARD_SIZE_STR, SettingsType.TYPE_NUMERIC, 3)

    def test_initial_boards_game_won(self):
        self.tester.generate_new_puzzle(self.test_settings, fixed_board=get_completed_board(),
                                        fixed_empty_spot=BoardPosition(2, 2))
        assert self.tester.game_won()

        self.tester.generate_new_puzzle(self.test_settings, fixed_board=get_almost_complete_board(),
                                        fixed_empty_spot=BoardPosition(2, 1))
        assert not self.tester.game_won()

    def test_game_won_with_move(self):
        self.tester.generate_new_puzzle(self.test_settings, fixed_board=get_almost_complete_board(),
                                        fixed_empty_spot=BoardPosition(2, 1))
        assert not self.tester.game_won()
        self.tester.move(consts.LEFT)
        assert self.tester.game_won()
        self.tester.move(consts.RIGHT)
        assert not self.tester.game_won()
        self.tester.move(consts.RIGHT)
        assert not self.tester.game_won()
