import surface as surface
from enum import IntEnum
from copy import deepcopy
import tile as tile
import pyraminxCache as Cache

# Standard enum for face, nothing special, matches color scheme from https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php


class orientation(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3

# swaps take place against the surface/face class, and have no association with contents or association between faces. Only the contents, a tile with an associated color
# can be changed by an operation or abstraction.

# important distinctions between encoding each face do exist. With the bottom face, the yellow face by arbitrary choice here, being encoded just as if you flipped the image on the website and counted
# top left to bottom right, which is every other face


class pyraminx:

    # list of faces, filled with our tuple values in order.
    

    def __init__(self):
        self.faces = [
            surface.surface("red"),
            surface.surface("green"),
            surface.surface("blue"),
            surface.surface("yellow")
        ]
        self.cache = []

    # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php encoding scheme chosen. U, u' etc.
    def clearCache(self):
        self.cache = []

    def encache(self):
        self.cache.append(self)
        
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

    def L(self):

        tempGreen = deepcopy(self.faces[orientation.GREEN])
        tempRed = deepcopy(self.faces[orientation.RED])
        tempYellow = deepcopy(self.faces[orientation.YELLOW])

        tile.swap_tile(self.faces[orientation.RED].tiles[6], tempGreen.tiles[1])
        tile.swap_tile(self.faces[orientation.RED].tiles[3], tempGreen.tiles[6])
        tile.swap_tile(self.faces[orientation.RED].tiles[7], tempGreen.tiles[7])
        tile.swap_tile(self.faces[orientation.RED].tiles[8], tempGreen.tiles[4])

        tile.swap_tile(self.faces[orientation.GREEN].tiles[6], tempYellow.tiles[3])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[5], tempYellow.tiles[7])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[4], tempYellow.tiles[8])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[1], tempYellow.tiles[6])

        tile.swap_tile(self.faces[orientation.YELLOW].tiles[8], tempGreen.tiles[8])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[7], tempGreen.tiles[7])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[6], tempGreen.tiles[6])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[3], tempGreen.tiles[3])
      

    #no way around it, just gotta suck it up and waste the memory
    def L_Prime(self):
       
        tempGreen = deepcopy(self.faces[orientation.GREEN])
        tempRed = deepcopy(self.faces[orientation.RED])
        tempYellow = deepcopy(self.faces[orientation.YELLOW])

        tile.swap_tile(self.faces[orientation.GREEN].tiles[1], tempRed.tiles[6])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[6], tempRed.tiles[3])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[7], tempRed.tiles[7])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[4], tempRed.tiles[8])

        tile.swap_tile(self.faces[orientation.YELLOW].tiles[3], tempGreen.tiles[6])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[7], tempGreen.tiles[5])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[8], tempGreen.tiles[4])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[6], tempGreen.tiles[1])

        tile.swap_tile(self.faces[orientation.RED].tiles[8], tempYellow.tiles[8])
        tile.swap_tile(self.faces[orientation.RED].tiles[7], tempYellow.tiles[7])
        tile.swap_tile(self.faces[orientation.RED].tiles[6], tempYellow.tiles[6])
        tile.swap_tile(self.faces[orientation.RED].tiles[3], tempYellow.tiles[3])



    def l(self):
         self.faces[orientation.RED].tiles[8],self.faces[orientation.GREEN].tiles[4], self.faces[orientation.YELLOW].tiles[8] = self.faces[orientation.YELLOW].tiles[8],self.faces[orientation.RED].tiles[8], self.faces[orientation.GREEN].tiles[4]

    def l_Prime(self):
        self.faces[orientation.YELLOW].tiles[8],self.faces[orientation.RED].tiles[8], self.faces[orientation.GREEN].tiles[4] = self.faces[orientation.RED].tiles[8],self.faces[orientation.GREEN].tiles[4], self.faces[orientation.YELLOW].tiles[8] 
   
    def R_Prime(self):

        tempGreen = deepcopy(self.faces[orientation.GREEN])
        tempYellow = deepcopy(self.faces[orientation.YELLOW])
        tempBlue  = deepcopy(self.faces[orientation.BLUE])

        tile.swap_tile(self.faces[orientation.GREEN].tiles[3], tempBlue.tiles[6])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[6], tempBlue.tiles[1])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[7], tempBlue.tiles[5])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[8], tempBlue.tiles[4])

        tile.swap_tile(self.faces[orientation.BLUE].tiles[1], tempYellow.tiles[1])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[4], tempYellow.tiles[4])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[5], tempYellow.tiles[5])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[6], tempYellow.tiles[6])

        tile.swap_tile(self.faces[orientation.YELLOW].tiles[1], tempGreen.tiles[6])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[4], tempGreen.tiles[8])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[5], tempGreen.tiles[7])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[6], tempGreen.tiles[3])
      

    #no way around it, just gotta suck it up and waste the memory
    def R(self):
       
        tempGreen = deepcopy(self.faces[orientation.GREEN])
        tempYellow = deepcopy(self.faces[orientation.YELLOW])
        tempBlue  = deepcopy(self.faces[orientation.BLUE])

        tile.swap_tile(self.faces[orientation.BLUE].tiles[6],tempGreen.tiles[3])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[1],tempGreen.tiles[6])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[5],tempGreen.tiles[7])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[4],tempGreen.tiles[8])

        tile.swap_tile(self.faces[orientation.YELLOW].tiles[1], tempBlue.tiles[1])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[4], tempBlue.tiles[4])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[5], tempBlue.tiles[5])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[6], tempBlue.tiles[6])

        tile.swap_tile(self.faces[orientation.GREEN].tiles[6], tempYellow.tiles[1])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[8], tempYellow.tiles[4])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[7], tempYellow.tiles[5])
        tile.swap_tile(self.faces[orientation.GREEN].tiles[3], tempYellow.tiles[6])

       
    def r(self):
        self.faces[orientation.YELLOW].tiles[4],self.faces[orientation.GREEN].tiles[8], self.faces[orientation.BLUE].tiles[4]  = self.faces[orientation.BLUE].tiles[4], self.faces[orientation.YELLOW].tiles[4], self.faces[orientation.GREEN].tiles[8]

    def r_Prime(self):
        self.faces[orientation.YELLOW].tiles[4],self.faces[orientation.GREEN].tiles[8], self.faces[orientation.BLUE].tiles[4] = self.faces[orientation.GREEN].tiles[8],self.faces[orientation.BLUE].tiles[4], self.faces[orientation.YELLOW].tiles[4] 
    
    def B(self):

        tempGreen = deepcopy(self.faces[orientation.GREEN])
        tempYellow = deepcopy(self.faces[orientation.YELLOW])
        tempBlue  = deepcopy(self.faces[orientation.BLUE])
        tempRed  = deepcopy(self.faces[orientation.RED])

        tile.swap_tile(self.faces[orientation.RED].tiles[1],tempBlue.tiles[6])
        tile.swap_tile(self.faces[orientation.RED].tiles[4],tempBlue.tiles[8])
        tile.swap_tile(self.faces[orientation.RED].tiles[5],tempBlue.tiles[7])
        tile.swap_tile(self.faces[orientation.RED].tiles[6],tempBlue.tiles[3])

        tile.swap_tile(self.faces[orientation.YELLOW].tiles[0], tempRed.tiles[4])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[1], tempRed.tiles[6])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[2], tempRed.tiles[5])
        tile.swap_tile(self.faces[orientation.YELLOW].tiles[3], tempRed.tiles[1])

        tile.swap_tile(self.faces[orientation.BLUE].tiles[3], tempYellow.tiles[1])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[6], tempYellow.tiles[3])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[7], tempYellow.tiles[2])
        tile.swap_tile(self.faces[orientation.BLUE].tiles[8], tempYellow.tiles[0])

    def B_Prime(self):
        pass