class Player:

    def __init__(self, x, y, floor):
        self.x = x
        self.y = y
        self.char = '@'
        self.current_floor = floor
        self.inventory = []


    def move(self, direction, scr):
        """Update player position both in the floor object and its own coordinates."""

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

        scr.addch(self.y, self.x, self.current_floor.tilelvl[self.y][self.x].terrain)

        if not self.coord_overflow(new_x, new_y) and self.current_floor.tilelvl[new_y][new_x].is_walkable:
            self.x = new_x
            self.y = new_y

        scr.addch(self.y, self.x, self.char)

    def coord_overflow(self, x, y):
        return x < 0 or x > (self.current_floor.width - 1) or y < 0 or y > (self.current_floor.height - 1);

