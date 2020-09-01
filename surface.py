import tile as tile
class surface:

    def __init__(self, color):

        self.tiles = []
        for i in range (16):
            self.tiles.append(tile.tile(color, i))