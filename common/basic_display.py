import texttable

class BasicDisplayUtils(object):

    def __init__(self):
        pass

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_table(table):
        t = texttable.Texttable()
        for i in range(0, len(table)):
            t.add_row([val for val in table[i]])
        print(t.draw())
