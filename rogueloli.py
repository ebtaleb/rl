#!/usr/bin/python

import curses

from player import Player
from floor import Floor

def curses_setup():

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)

    return stdscr

def curses_cleanup(stdscr):

    curses.nocbreak()
    curses.curs_set(1)
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

def initialize_player(x, y, floor, scr):
    p = Player(x, y, floor)
    scr.addch(p.y, p.x, p.char)
    floor.tilelvl[p.y][p.x].player_presence = p

    return p

def initialize_floor(h, w, scr):
    floor = Floor(h, w)
    scr.addstr(0, 0, floor.stringlvl)

    return floor

def initialize_items(nb, floor):
    pass

def initialize_dungeon():
    pass

def init():

    try:
        screen = curses_setup()
        height, width = screen.getmaxyx()
        x = width // 2
        y = height // 2

        floor = initialize_floor(40, 60, screen)
        player = initialize_player(30, 20, floor, screen)
    except curses.error:
        pass
    finally:
        return screen, player, floor

def main():

    screen, p, floor = init()

    try:
        while 1:

            ch = chr(screen.getch())

            if ch == 'q':
                break

            p.move(ch, screen)
            screen.refresh()

    except curses.error:
        pass

    finally:
        curses_cleanup(screen)

if __name__ == '__main__':
    main()
