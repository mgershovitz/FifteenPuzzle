import unittest
from fifteenpuzzle.board_utils.board_generator import RandomBoardGenerator

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board_size = 3
        self.test_empty_spot = [2,2]
        self.tester = RandomBoardGenerator(self.test_board_size)

    def test_generate_board_unique(self):
        boards_number = 10
        boards = []
        for i in range(0, boards_number):
            new_board = self.tester.generate_board(difficulty=5)
            assert new_board not in boards
            boards.append(new_board)
