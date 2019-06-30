import unittest

import copy
from board_utils.matrix_board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_board_size = 3
        self.test_empty_spot = [2,2]
        self.tester = Board(self.test_board_size, self.test_empty_spot)

    def test_get_new_randomized_board_unique(self):
        boards_number = 10
        boards = []
        for i in range(0, boards_number):
            self.tester.get_new_randomized_board()
            new_board = copy.deepcopy(self.tester.board)
            assert new_board not in boards
            boards.append(new_board)
