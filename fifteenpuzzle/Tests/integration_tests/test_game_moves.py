import unittest

from fifteenpuzzle.common import consts
from fifteenpuzzle.game_logic import PuzzleGame
from fifteenpuzzle.settings.settings import GameSettingsManager, SettingsType


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.tester = PuzzleGame()
        self.test_settings = GameSettingsManager()
        self.test_settings.load_settings()

    def test_game_move_in_all_directions(self):
        self.test_settings.set(consts.BOARD_SIZE_STR, SettingsType.TYPE_NUMERIC, 3)
        self.tester.generate_new_puzzle(self.test_settings)

        first_empty_spot = self.tester.game_board.empty_spot
        empty_spot_left_neighbour = first_empty_spot.get_left_neighbour()

        self.tester.move(consts.RIGHT)
        current_empty_spot = self.tester.game_board.empty_spot
        assert current_empty_spot == empty_spot_left_neighbour
        empty_spot_above_neighbour = current_empty_spot.get_above_neighbour()

        self.tester.move(consts.DOWN)
        current_empty_spot = self.tester.game_board.empty_spot
        assert current_empty_spot == empty_spot_above_neighbour
        empty_spot_right_neighbour = current_empty_spot.get_right_neighbour()

        self.tester.move(consts.LEFT)
        current_empty_spot = self.tester.game_board.empty_spot
        assert current_empty_spot == empty_spot_right_neighbour

    def test_game_ignore_impossible_moves(self):
        self.tester.generate_new_puzzle(self.test_settings)

        first_empty_spot = self.tester.game_board.empty_spot
        empty_spot_right_neighbour = first_empty_spot.get_right_neighbour()

        #since the default empty spot is also the right most bottom corener, a "left move" won't affect it
        self.tester.move(consts.LEFT)
        current_empty_spot = self.tester.game_board.empty_spot
        assert current_empty_spot == first_empty_spot
        assert current_empty_spot != empty_spot_right_neighbour
