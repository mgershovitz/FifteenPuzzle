from common import consts


class RandomBoardGenerator(object):
    def __init__(self, board_size):
        self.board_size = board_size

    def generate_board(self, empty_spot):
        n = 1
        board = list()
        for i in range(0, self.board_size):
            board.append(list())
            for j in range(0, self.board_size):
                if empty_spot[0] == i and empty_spot[1] == j:
                    board[i].append(consts.EMPTY_STR)
                else:
                    board[i].append(n)
                    n += 1

        return board
