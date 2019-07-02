import unittest

from fifteenpuzzle.common import consts
from fifteenpuzzle.game_logic import PuzzleGame
from fifteenpuzzle.settings.settings import GameSettingsManager, SettingsType


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.tester = PuzzleGame()
        self.test_settings = GameSettingsManager()
        self.test_settings.load_settings()

    def test_game_board_size(self):
        self.test_settings.set(consts.BOARD_SIZE_STR, SettingsType.TYPE_NUMERIC, 2)
        self.tester.generate_new_puzzle(self.test_settings)
        board = self.tester.game_board.board
        assert len(board) == 2

        self.test_settings.set(consts.BOARD_SIZE_STR, SettingsType.TYPE_NUMERIC, 3)
        self.tester.generate_new_puzzle(self.test_settings)
        board = self.tester.game_board.board
        assert len(board) == 3

        self.test_settings.set(consts.BOARD_SIZE_STR, SettingsType.TYPE_NUMERIC, 2)
        self.tester.generate_new_puzzle(self.test_settings)
        board = self.tester.game_board.board
        assert len(board) == 2