import curses
import sys

class Display:

    def __init__(self, loggers):
        self.__screen = None
        self.__loggers = loggers
        self.__to_be_displayed = set()

    def setup(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        stdscr.keypad(1)

        self.__screen = stdscr

    def cleanup(self):
        curses.nocbreak()
        curses.curs_set(1)
        self.__screen.keypad(0)
        curses.echo()
        curses.endwin()

        sys.exit(0)

    def add_item_to_display(self, obj):
        self.__to_be_displayed.add(obj)

    def remove_from_display(self, obj):
        self.__to_be_displayed.discard(obj)

    def print_to_display(self, x, y, string):
        try:
            self.__screen.addstr(x, y, string)
        except curses.error:
            pass

    def refresh(self):
        self.__screen.refresh()

    def get_char(self):
        return chr(self.__screen.getch())

    def display(self):
        for obj in self.__to_be_displayed:
            self.__screen.addch(obj.y, obj.x, obj.char)

    def clear(self):
        for obj in self.__to_be_displayed:
            self.__screen.addch(obj.y, obj.x, '.')
