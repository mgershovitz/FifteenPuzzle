import texttable

class BasicDisplayUtils(object):

    def __init__(self):
        pass

    def init_display(self):
        pass

    def get_user_input(self):
        return str(input())

    def display_message(self, message):
        print(message)

    def display_game_board(self, board):
        t = texttable.Texttable()
        for i in range(0, len(board)):
            t.add_row([val for val in board[i]])
        print(t.draw())
