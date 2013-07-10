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

def init():

    try:
        screen = curses_setup()
        height, width = screen.getmaxyx()
        x = width // 2
        y = height // 2
        floor = Floor(40, 60)
        player = Player(30, 20, floor)

        screen.addstr(0, 0, floor.stringlvl)
        screen.addch(player.y, player.x, player.char)
    except curses.error:
        screen.addstr(0, 0, floor.stringlvl)
        screen.addch(player.y, player.x, player.char)
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
