class BoardPosition(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_adj_left(self):
        return BoardPosition(self.x, self.y - 1)

    def get_adj_right(self):
        return BoardPosition(self.x, self.y + 1)

    def get_adj_up(self):
        return BoardPosition(self.x - 1, self.y)

    def get_adj_down(self):
        return BoardPosition(self.x + 1, self.y)

    def is_valid_board_position(self, board_size):
        return 0 <= self.x <= board_size - 1 and 0 <= self.y <= board_size - 1

    @classmethod
    def get_position_from_indexes_tuple(cls, pos_tuple):
        return BoardPosition(pos_tuple[0], pos_tuple[1])
