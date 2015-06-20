import logging

class Player:

    def __init__(self, x, y, floor):
        self.x = x
        self.y = y
        self.char = '@'
        self.current_floor = floor
        self.inventory = set()
        self.current_floor.tilelvl[y][x].player_presence = True
        self.logger = logging.getLogger('player')
        self.logger.info("Player instanciated.")

    def move(self, direction):
        """Update player position."""

        if direction == '8':
            new_x = self.x
            new_y = self.y - 1
        elif direction == '4':
            new_x = self.x - 1
            new_y = self.y
        elif direction == '2':
            new_x = self.x
            new_y = self.y + 1
        elif direction == '6':
            new_x = self.x + 1
            new_y = self.y
        elif direction == '7':
            new_x = self.x - 1
            new_y = self.y - 1
        elif direction == '9':
            new_x = self.x + 1
            new_y = self.y - 1
        elif direction == '1':
            new_x = self.x - 1
            new_y = self.y + 1
        elif direction == '3':
            new_x = self.x + 1
            new_y = self.y + 1
        else:
            return

        if not self.coord_overflow(new_x, new_y) and self.current_floor.tilelvl[new_y][new_x].is_walkable:
            self.current_floor.tilelvl[self.y][self.x].player_presence = False
            self.x = new_x
            self.y = new_y
            self.current_floor.tilelvl[new_y][new_x].player_presence = True

        self.logger.info("Currently at ("+ str(new_x) + ", " + str(new_y) + ")")

    def coord_overflow(self, x, y):
        return x < 0 or x > (self.current_floor.width - 1) or y < 0 or y > (self.current_floor.height - 1);

    def get_object_on_floor(self):
        try:
            obj = self.current_floor.remove_object(self.x, self.y)
            obj.x = -1
            obj.y = -1
            obj.owner = self
            self.inventory.add(obj)
            self.logger.info("Got a " + obj.name)
            return obj
        except AttributeError:
            pass

    def put_object_on_floor(self, obj):
        try:
            popped_item = self.inventory.pop()
            popped_item.x = self.x
            popped_item.y = self.y
            popped_item.owner = None
            self.current_floor.put_object(popped_item, self.x, self.y)
            self.logger.info("Dropped a " + popped_item.name)
            self.logger.info("Dropped a " + popped_item.name)
            return popped_item
        except KeyError:
            pass

