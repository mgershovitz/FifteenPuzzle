import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

screen.addstr(0, 0, "hello")
screen.getch()

curses.nocbreak()
screen.keypad(0)
curses.echo()
curses.endwin()
