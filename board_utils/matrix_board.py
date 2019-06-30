from common import consts

class Board(object):
    def __init__(self, board_size, empty_spot):
        self.board = None
        self.board_size = board_size
        self.empty_spot = BoardPosition.get_position_from_indexes_tuple(empty_spot)

    def get_new_randomized_board(self,):
        n = 1
        self.board = list()
        for i in range(0, self.board_size):
            self.board.append(list())
            for j in range(0, self.board_size):
                if self.empty_spot.x == i and self.empty_spot.y == j:
                    self.board[i].append(consts.EMPTY_STR)
                else:
                    self.board[i].append(n)
                    n += 1

    def get(self, pos):
        if self.is_valid_board_position(pos):
            return self.board[pos.x][pos.y]

    def set(self, pos, val):
        if self.is_valid_board_position(pos):
            self.board[pos.x][pos.y] = val
            return 1
        return 0

    def position_matches_value(self, pos):
        return self.board[pos.x][pos.y] == pos.x * self.board_size + pos.y + 1

    def is_valid_board_position(self, pos):
        return 0 <= pos.x <= self.board_size - 1 and 0 <= pos.y <= self.board_size - 1

    def set_empty_spot(self, pos):
        self.empty_spot = pos
        self.set(pos, consts.EMPTY_STR)

    def get_neighbour_by_direction(self, direction):
        if direction == consts.RIGHT:
            return self.empty_spot.get_left_neighbour()
        elif direction == consts.LEFT:
            return self.empty_spot.get_right_neighbour()
        elif direction == consts.UP:
            return self.empty_spot.get_bellow_neighbour()
        elif direction == consts.DOWN:
            return self.empty_spot.get_above_neighbour()

    def execute_move(self, direction):
        neighbour_pos = self.get_neighbour_by_direction(direction)
        if not neighbour_pos:
            raise Exception

        neighbour_val = self.get(neighbour_pos)
        if neighbour_val:
            original_empty_spot = self.empty_spot
            self.set(original_empty_spot, neighbour_val)
            self.set_empty_spot(neighbour_pos)

            return original_empty_spot, neighbour_pos

    def get_tile_right_to_empty_spot(self):
        if self.empty_spot.y < self.board_size - 1:
            return self.board[self.empty_spot.x][self.empty_spot.y + 1]

    def get_tile_bellow_empty_spot(self):
        if self.empty_spot.x < self.board_size - 1:
            return self.board[self.empty_spot.x + 1][self.empty_spot.y]

class BoardPosition(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_right_neighbour(self):
        return BoardPosition(self.x, self.y + 1)

    def get_left_neighbour(self):
        return BoardPosition(self.x, self.y - 1)

    def get_above_neighbour(self):
        return BoardPosition(self.x - 1, self.y)

    def get_bellow_neighbour(self):
        return BoardPosition(self.x + 1, self.y)

    def __repr__(self):
        return "(%d/%d)" % (self.x, self.y)

    def __hash__(self):
        return int(str(self.x) + str(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @classmethod
    def get_position_from_indexes_tuple(cls, pos_tuple):
        return BoardPosition(pos_tuple[0], pos_tuple[1])
