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

def initialize_floor(h, w):
    floor = Floor(h, w)

    try:
        screen.addstr(0, 0, floor.stringlvl)
    except curses.error:
        pass

    return floor

def initialize_items(nb, floor):
    pass

def initialize_dungeon():
    pass

screen = curses_setup()
floor = initialize_floor(40, 60)
p = Player(30, 20, floor)

to_be_displayed = [p]

def display():
    for obj in to_be_displayed:
        screen.addch(obj.y, obj.x, obj.char)

def clear():
    for obj in to_be_displayed:
        screen.addch(obj.y, obj.x, '.')

def main():

    try:
        while 1:

            display()

            ch = chr(screen.getch())

            if ch == 'q':
                break

            clear()
            p.move(ch)
            #clear()    TODO: why is there no clean if clear is put there? to be investigated
            screen.refresh()

    finally:
        curses_cleanup(screen)

if __name__ == '__main__':
    main()
