from tile import Tile

class Floor:

    def __init__(self, height, width):

        self.height = height
        self.width = width

        wall = '#' * width
        space = '#' + '.' * (width - 2) + '#'

        self.tilelvl = [[None for i in range(width)] for j in range(height)]

        for i in range(width):
            self.tilelvl[0][i] = Tile('#')
            self.tilelvl[height-1][i] = Tile('#')

        j = 0
        for i in range(1, height-1):
            for char in space:
                self.tilelvl[i][j] = Tile(space[j])
                j += 1
            j = 0

        self.stringlvl = wall + '\n'
        for i in range(1, height - 1):
            self.stringlvl += space + '\n'
        self.stringlvl += wall + '\n'

    def put_object(self, obj, x, y):
        self.tilelvl[y][x].objects.insert(0, obj)

    def remove_object(self, x, y):
        if self.tilelvl[y][x].objects:
            return self.tilelvl[y][x].objects.pop(0)
