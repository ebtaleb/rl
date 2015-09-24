class MapHandler:

    def __init__(self, w, h, percent_are_walls):
        self.width = w
        self.height = h
        self.tile_map = [[None for i in range(w)] for j in range(h)]
        self.percent_are_walls = percent_are_walls

    def make_caverns(self):

        column = 0
        row = 0
        while row <= self.height - 1:
            while column <= self.width - 1:
                self.tile_map[column][row] = self.place_wall_logic(column, row)
                column = column + 1
            row = row + 1

        #for row in range(0, self.height - 1):
            #for column in range(0, self.width - 1):
                #tile_map[column][row] = self.place_wall_logic(column, row)

    def place_wall_logic(self, x, y):

        num_walls = self.get_adjacent_walls(x, y, 1, 1)

        if self.tile_map[x][y] == 1:  # if the tile is a wall

            if num_walls >= 4:
                return 1

            if num_walls < 2:
                return 0

        else:
            if num_walls >= 5:
                return 1

        return 0

    def get_adjacent_walls(self, x, y, scope_x, scope_y):

        start_x = x - scope_x
        start_y = y - scope_y
        end_x = x + scope_x
        end_y = y + scope_y

        wall_counter = 0

        for iy in range(start_y, end_y):
            for ix in range(start_x, end_x):

                if not (ix == x and iy == y):

                    if self.is_wall(ix, iy):
                        wall_counter = wall_counter + 1
        return wall_counter

    def is_wall(self, x, y):
        if self.is_out_of_bounds(x, y) or self.tile_map[x][y] == 1:
            return True
        if self.tile_map[x][y] == 0:
            return False
        return False

    def is_out_of_bounds(self, x, y):
        if x < 0 or y < 0:
            return True
        elif x > self.width - 1 or y > self.height - 1:
            return True
        return False

    def print_map(self):
        print(self.map_to_string())

    def map_to_string(self):
        return

    def random_fill_map(self):

        map_middle = 0

        for row in range(0, self.height):
            for column in range(0, self.width):

                if column == 0 or column == self.width - 1:
                    self.tile_map[column][row] = 1

                elif row == 0 or row == self.height - 1:
                    self.tile_map[column][row] = 1

                else:

                    map_middle = self.height / 2

                    if row == map_middle:
                        self.tile_map[column][row] = 0
                    else:
                        self.tile_map[column][row] = self.random_percent()

    def random_percent(self):
        if rand.randrange(1, 101) < self.percent_are_walls:
            return 1
        return 0
