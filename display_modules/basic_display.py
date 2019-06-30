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

    def display_table(self, table):
        t = texttable.Texttable()
        for i in range(0, len(table)):
            t.add_row([val for val in table[i]])
        print(t.draw())
