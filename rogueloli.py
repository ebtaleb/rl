#!/usr/bin/python

import curses

import logging
import logging.config
import os

from player import Player
from floor import Floor
from item import Item

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

def initialize_items(nb):

    items = []

    for i in range(1, nb):
        current = Item("Obj"+str(nb), 'I', None, i, i)
        items.append(current)
        to_be_displayed.append(current)

    return items

def initialize_dungeon():
    pass

def display():
    for obj in to_be_displayed:
        screen.addch(obj.y, obj.x, obj.char)

def clear():
    for obj in to_be_displayed:
        screen.addch(obj.y, obj.x, '.')

screen = curses_setup()
floor = initialize_floor(40, 60)

to_be_displayed = []
list_of_items = initialize_items(5)

def main():

    if not os.path.exists("playerpipe"):
        os.mkfifo("playerpipe")

    if not os.path.exists("itempipe"):
        os.mkfifo("itempipe")

    logging.config.fileConfig("log.conf", disable_existing_loggers=False)

    player_log = logging.getLogger("player")
    item_log = logging.getLogger("item")

    p = Player(30, 20, floor)
    to_be_displayed.append(p)

    try:
        while 1:

            display()

            ch = chr(screen.getch())

            if ch == 'q':
                break

            clear()
            p.move(ch)
            screen.refresh()

    except KeyboardInterrupt:
        pass
    finally:
        curses_cleanup(screen)
        os.remove("playerpipe")
        os.remove("itempipe")

if __name__ == '__main__':
    main()
