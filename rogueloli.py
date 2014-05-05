#!/usr/bin/python

import logging
import logging.config
import os

from player import Player
from floor import Floor
from item import Item
from display import Display

def initialize_floor(h, w, d):
	floor = Floor(h, w)
	d.print_to_display(0, 0, floor.stringlvl)
	return floor

def initialize_items(nb, d):

	items = []

	for i in range(1, nb):
		current = Item("Obj"+str(nb), 'I', None, i, i)
		items.append(current)
		d.add_item_to_display(current)
		floor.put_object(current, current.x, current.y)

	return items

def get(p, display):

	item_to_display = p.get_object_on_floor()
	display.remove_from_display(item_to_display)

def put(p, display):

	item_to_display = p.put_object_on_floor(None)
	if item_to_display is not None:
		display.add_item_to_display(item_to_display)

def initialize_logging(disable_loggers):

    if not disable_loggers:

        if not os.path.exists("playerpipe"):
            os.mkfifo("playerpipe")

        if not os.path.exists("itempipe"):
            os.mkfifo("itempipe")

    logging.config.fileConfig("log.conf", disable_existing_loggers=disable_loggers)

display = Display("log")
display.setup()

floor = initialize_floor(40, 60, display)

list_of_items = initialize_items(5, display)

action_dict = { 'q' : display.cleanup,
		'g' : get,
		'p' : put }

def main():

    disable_loggers = True
    initialize_logging(disable_loggers)

    p = Player(30, 20, floor)
    display.add_item_to_display(p)

    try:
        while 1:

            display.display()

            ch = display.get_char()

            if ch in "pg":
                action_dict[ch](p, display)

            if ch == 'q':
                action_dict[ch]()

            display.clear()
            if ch in "123456789":
                p.move(ch)
            display.refresh()

    except KeyboardInterrupt:
        pass
    finally:
        if not disable_loggers:
            os.remove("playerpipe")
            os.remove("itempipe")
        display.cleanup()

if __name__ == '__main__':
    main()
