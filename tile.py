class Tile:
    """
    A tile is a basic displayable unit.
    """

    walkables = {'#' : False, '.' : True}

    def __init__(self, char):

        self.terrain = char
        self.is_walkable = self.walkables[char]

        self.items = []

        self.player = None
        self.monster = None

