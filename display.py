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

    def inven(self):

# Set up the window
        quote_window = curses.newwin(curses.LINES-2, curses.COLS, 1, 0)

        quote_text_window = quote_window.subwin(curses.LINES-6, curses.COLS-4, 3, 2)

        quote_text_window.addstr("Press 'R' to be a faggot")

# Draw a border around the main quote window
        quote_window.box()

# Update the internal window data structures
        self.__screen.noutrefresh()
        quote_window.noutrefresh()

# Redraw the screen
        curses.doupdate()

# Create the event loop
        while True:
            c = quote_text_window.getch()

            if c == ord('r') or c == ord('R'):
                quote_text_window.clear()
                quote_text_window.addstr("Getting a faggot...")

                quote_text_window.refresh()
                quote_text_window.clear()
                quote_text_window.addstr("U R A FAGGOT")

            elif c == ord('q') or c == ord('Q'):
                break

            # Refresh the windows from the bottom up
            self.__screen.noutrefresh()
            quote_window.noutrefresh()
            quote_text_window.noutrefresh()
            curses.doupdate()


        #self.__screen.noutrefresh()
        #curses.doupdate()

