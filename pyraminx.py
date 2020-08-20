import surface as surface
from enum import IntEnum

# Standard enum for face, nothing special, matches color scheme from https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php


class orientation(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3

# swaps take place against the surface/face class, and have no association with contents or association between faces. Only the contents, a tile with an associated color
# can be changed by an operation or abstraction.

# important distinctions between encoding each face do exist. With the bottom face, the yellow face by arbitrary choice here, being encoded just as if you flipped the image on the website and counted
# top left to bottom right, whhich is every other face


class pyraminx:

    # list of faces, filled with our tuple values in order.
    faces = []

    def __init__(self):
        self.faces = [
            surface.surface("red"),
            surface.surface("green"),
            surface.surface("blue"),
            surface.surface("yellow")
        ]

    # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php encoding scheme chosen. U, u' etc.

    def U(self):
        for i in range(4):
            self.faces[orientation.RED].tiles[i],    self.faces[orientation.GREEN].tiles[i],   self.faces[orientation.BLUE].tiles[
                i] = self.faces[orientation.GREEN].tiles[i],  self.faces[orientation.BLUE].tiles[i],  self.faces[orientation.RED].tiles[i]

    def U_Prime(self):
        for i in range(4):
            self.faces[orientation.RED].tiles[i], self.faces[orientation.GREEN].tiles[i], self.faces[orientation.BLUE].tiles[
                i] = self.faces[orientation.BLUE].tiles[i], self.faces[orientation.RED].tiles[i], self.faces[orientation.GREEN].tiles[i]

    def u(self):
        self.faces[orientation.RED].tiles[0],  self.faces[orientation.GREEN].tiles[0], self.faces[orientation.BLUE].tiles[
            0] = self.faces[orientation.GREEN].tiles[0], self.faces[orientation.BLUE].tiles[0], self.faces[orientation.RED].tiles[0]

    def u_Prime(self):
        self.faces[orientation.RED].tiles[0], self.faces[orientation.GREEN].tiles[0], self.faces[orientation.BLUE].tiles[
            0] = self.faces[orientation.BLUE].tiles[0],  self.faces[orientation.RED].tiles[0], self.faces[orientation.GREEN].tiles[0]
