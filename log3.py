#!/usr/bin/python

import logging
import logging.config
import os
import time

def main():

    if not os.path.exists("playerpipe"):
        os.mkfifo("playerpipe")

    if not os.path.exists("itempipe"):
        os.mkfifo("itempipe")

    logging.config.fileConfig("log.conf", disable_existing_loggers=False)

    player_log = logging.getLogger("player")
    item_log = logging.getLogger("item")

    try:
        while True:
            player_log.info("ping")
            time.sleep(2)
            item_log.info("pong")
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    finally:
        os.remove("playerpipe")
        os.remove("itempipe")

if __name__ == "__main__":
    main()

