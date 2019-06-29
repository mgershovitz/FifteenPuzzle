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