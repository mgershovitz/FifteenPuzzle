import unittest

from common import consts
from game_logic import PuzzleGame
from settings.settings import SettingsType
from settings.game_settings import GameSettingsManager


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.tester = PuzzleGame()
        self.test_settings = GameSettingsManager()
        self.test_settings.load_settings()

    def test_game_board_size(self):
        self.test_settings.set(consts.BOARD_SIZE_STR, SettingsType.TYPE_NUMERIC, 4)
        self.tester.generate_new_puzzle(self.test_settings)
        board = self.tester.game_board.board
        assert len(board) == 4

        self.test_settings.set(consts.BOARD_SIZE_STR, SettingsType.TYPE_NUMERIC, 3)
        self.tester.generate_new_puzzle(self.test_settings)
        board = self.tester.game_board.board
        assert len(board) == 3

        self.test_settings.set(consts.BOARD_SIZE_STR, SettingsType.TYPE_NUMERIC, 4)
        self.tester.generate_new_puzzle(self.test_settings)
        board = self.tester.game_board.board
        assert len(board) == 4