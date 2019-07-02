import unittest
from board_utils.board_generator import RandomBoardGenerator
from board_utils.matrix_board import BoardPosition
from common import consts


class TestBoardGenerator(unittest.TestCase):
    def setUp(self):
        self.test_board_size = 3
        self.test_empty_spot = [2,2]
        self.tester = RandomBoardGenerator()
        self.tester.reset_board_size(self.test_board_size)

    def test_generate_board_unique(self):
        boards_number = 10
        boards = []
        for i in range(0, boards_number):
            new_board = self.tester.generate_board(difficulty=5)
            assert new_board not in boards
            boards.append(new_board)

    def test_board_is_solvable(self):
        #solvability check is based on this articel -
        # https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html

        # Condition 1 - even width + empty spot is on odd row from bottom
        new_board_size = 4
        self.tester.reset_board_size(new_board_size)
        new_board = self.tester.generate_board(difficulty=5)
        board_inversions = self.count_inversions(new_board, new_board_size)
        assert board_inversions % 2 == 0

        # Condition 1 - odd width
        new_board_size = 3
        self.tester.reset_board_size(new_board_size)
        new_board = self.tester.generate_board(difficulty=5)
        board_inversions = self.count_inversions(new_board, new_board_size)
        assert board_inversions % 2 == 0

    def count_inversions(self, board, board_size):
        seen_values = []
        inversions = 0
        for i in reversed(range(0, board_size)):
            for j in reversed(range(0, board_size)):
                cell_val = board.get(BoardPosition(i,j))
                if cell_val == consts.EMPTY_STR:
                    continue
                for val in seen_values:
                    if val < cell_val:
                        inversions += 1
                seen_values.append(cell_val)

        return inversions



