import surface as surface
from enum import IntEnum
from copy import deepcopy
import tile as tile
import asciiCache as asciiCache
import random as random

try:
    from colorama import Fore, Back, Style, init
except ImportError as e:
    print("Error, missing package colorama, pip3 install colorama to resolve")

init()
asciiCache = asciiCache.asciiCache()

# Standard enum for face matching the colors from the reference https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php simulator. 
class orientation(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3

# swaps take place against the surface/face class, and have no association with contents or association between faces. Only the contents, a tile with an associated color
# can be changed by an operation or abstraction.

# important distinctions between encoding each face do exist. With the bottom face, the yellow face by arbitrary choice here, being encoded just as if you flipped the image on the website and counted
# top left to bottom right, which is every other face

# slight memory issues exist with about 90 bytes of wasted space per face swap. This is acceptable on my home machine as I have 32g of ram.
# this may not be possible to run if lots of memory allocations are done/lots of waste is encompassed.

# https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php encoding scheme chosen. U, u' etc. All code is original, albeit likely to be similar to code that does the same thing
# as there are only a finite number of ways to encode these operations. I only consulted the visual changes of this web applet to do the following functions, and furthermore
# used my unit testing before writing the visualizer for "sanity checks" as it was a thousand times faster to just draw things out on paper and then go from there in testing
# in terms of time commitment.

class pyraminx:

    # list of faces, filled with our tuple values in order.
    
    # Initialize object with faces and colors consistent with the enum
    def __init__(self):
        self.faces = [
            surface.surface("red"),
            surface.surface("green"),
            surface.surface("blue"),
            surface.surface("yellow")
        ]
        self.cache = []
        
    
    # Clear all instances of the pyraminx from the cache
    def clearCache(self):
        self.cache = []
   
    # Add the current instance of the pyraminx to the cache
    def encache(self):
        self.cache.append(self)
   
    # Perform the U action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Roughly rotates entire top section.
    def U(self):
        for i in range(4):
            self.faces[orientation.RED].tiles[i],    self.faces[orientation.GREEN].tiles[i],   self.faces[orientation.BLUE].tiles[
                i] = self.faces[orientation.GREEN].tiles[i],  self.faces[orientation.BLUE].tiles[i],  self.faces[orientation.RED].tiles[i]
   
    # Perform the U' action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Roughly rotates the entire top section the opposite direction.
    def U_Prime(self):
        for i in range(4):
            self.faces[orientation.RED].tiles[i], self.faces[orientation.GREEN].tiles[i], self.faces[orientation.BLUE].tiles[
                i] = self.faces[orientation.BLUE].tiles[i], self.faces[orientation.RED].tiles[i], self.faces[orientation.GREEN].tiles[i]
    
    def Uw(self):
        for i in range(9):
            self.faces[orientation.RED].tiles[i],    self.faces[orientation.GREEN].tiles[i],   self.faces[orientation.BLUE].tiles[
                i] = self.faces[orientation.GREEN].tiles[i],  self.faces[orientation.BLUE].tiles[i],  self.faces[orientation.RED].tiles[i]
   
    # Perform the U' action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Roughly rotates the entire top section the opposite direction.
    def Uw_Prime(self):
        for i in range(9):
            self.faces[orientation.RED].tiles[i], self.faces[orientation.GREEN].tiles[i], self.faces[orientation.BLUE].tiles[
                i] = self.faces[orientation.BLUE].tiles[i], self.faces[orientation.RED].tiles[i], self.faces[orientation.GREEN].tiles[i]
  
    # Perform the u action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Rotates the top corner. 
    def u(self):
        self.faces[orientation.RED].tiles[0],  self.faces[orientation.GREEN].tiles[0], self.faces[orientation.BLUE].tiles[
            0] = self.faces[orientation.GREEN].tiles[0], self.faces[orientation.BLUE].tiles[0], self.faces[orientation.RED].tiles[0]
   
    # Perform the u action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Rotates the top corner
    def u_Prime(self):
        self.faces[orientation.RED].tiles[0], self.faces[orientation.GREEN].tiles[0], self.faces[orientation.BLUE].tiles[
            0] = self.faces[orientation.BLUE].tiles[0],  self.faces[orientation.RED].tiles[0], self.faces[orientation.GREEN].tiles[0]
   
    # Perform the L action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Rotates the left tripiece roughly from the front.
    def L_Prime(self):

        
        self.faces[orientation.GREEN].tiles[4], self.faces[orientation.RED].tiles[13] =  self.faces[orientation.RED].tiles[13], self.faces[orientation.GREEN].tiles[4] 
        self.faces[orientation.GREEN].tiles[10], self.faces[orientation.RED].tiles[14] =  self.faces[orientation.RED].tiles[14], self.faces[orientation.GREEN].tiles[10] 
        self.faces[orientation.GREEN].tiles[11], self.faces[orientation.RED].tiles[8] =  self.faces[orientation.RED].tiles[8], self.faces[orientation.GREEN].tiles[11] 
        self.faces[orientation.GREEN].tiles[9], self.faces[orientation.RED].tiles[15] =  self.faces[orientation.RED].tiles[15], self.faces[orientation.GREEN].tiles[9] 

        self.faces[orientation.YELLOW].tiles[8], self.faces[orientation.GREEN].tiles[11] = self.faces[orientation.GREEN].tiles[11], self.faces[orientation.YELLOW].tiles[8] 
        self.faces[orientation.YELLOW].tiles[13], self.faces[orientation.GREEN].tiles[4] = self.faces[orientation.GREEN].tiles[4], self.faces[orientation.YELLOW].tiles[13] 
        self.faces[orientation.YELLOW].tiles[14], self.faces[orientation.GREEN].tiles[9] = self.faces[orientation.GREEN].tiles[9], self.faces[orientation.YELLOW].tiles[14] 
        self.faces[orientation.YELLOW].tiles[15], self.faces[orientation.GREEN].tiles[10] = self.faces[orientation.GREEN].tiles[10], self.faces[orientation.YELLOW].tiles[15] 
    
    def Lw_Prime(self):
        self.Lw()
        self.Lw()

    
    def L(self):
       
        self.faces[orientation.RED].tiles[13] , self.faces[orientation.GREEN].tiles[4]   = self.faces[orientation.GREEN].tiles[4],  self.faces[orientation.RED].tiles[13]
        self.faces[orientation.RED].tiles[14] , self.faces[orientation.GREEN].tiles[10]  = self.faces[orientation.GREEN].tiles[10], self.faces[orientation.RED].tiles[14]
        self.faces[orientation.RED].tiles[8]  ,  self.faces[orientation.GREEN].tiles[11] = self.faces[orientation.GREEN].tiles[11], self.faces[orientation.RED].tiles[8]
        self.faces[orientation.RED].tiles[15] , self.faces[orientation.GREEN].tiles[9]   = self.faces[orientation.GREEN].tiles[9],  self.faces[orientation.RED].tiles[15]

        self.faces[orientation.YELLOW].tiles[8],self.faces[orientation.RED].tiles[8] =  self.faces[orientation.RED].tiles[8], self.faces[orientation.YELLOW].tiles[8]
        self.faces[orientation.YELLOW].tiles[13],self.faces[orientation.RED].tiles[13] =  self.faces[orientation.RED].tiles[13], self.faces[orientation.YELLOW].tiles[13]
        
        self.faces[orientation.RED].tiles[14], self.faces[orientation.YELLOW].tiles[15] = self.faces[orientation.YELLOW].tiles[15], self.faces[orientation.RED].tiles[14]
        self.faces[orientation.YELLOW].tiles[14], self.faces[orientation.RED].tiles[15] = self.faces[orientation.RED].tiles[15], self.faces[orientation.YELLOW].tiles[14]
    
    ##Bug Watch
    def Lw(self):
        self.L()


        self.faces[orientation.GREEN].tiles[1],  self.faces[orientation.RED].tiles[11] = self.faces[orientation.RED].tiles[11] , self.faces[orientation.GREEN].tiles[1]
        self.faces[orientation.GREEN].tiles[5],  self.faces[orientation.RED].tiles[12] = self.faces[orientation.RED].tiles[12] , self.faces[orientation.GREEN].tiles[5]
        self.faces[orientation.GREEN].tiles[6],  self.faces[orientation.RED].tiles[6]  = self.faces[orientation.RED].tiles[6]  , self.faces[orientation.GREEN].tiles[6]
        self.faces[orientation.GREEN].tiles[12], self.faces[orientation.RED].tiles[7]  = self.faces[orientation.RED].tiles[7]  , self.faces[orientation.GREEN].tiles[12]
        self.faces[orientation.GREEN].tiles[13], self.faces[orientation.RED].tiles[3]  = self.faces[orientation.RED].tiles[3]  , self.faces[orientation.GREEN].tiles[13]

        self.faces[orientation.RED].tiles[3],self.faces[orientation.YELLOW].tiles[3] =  self.faces[orientation.YELLOW].tiles[3],self.faces[orientation.RED].tiles[3]
        self.faces[orientation.RED].tiles[7],self.faces[orientation.YELLOW].tiles[7] =  self.faces[orientation.YELLOW].tiles[7],self.faces[orientation.RED].tiles[7]
        self.faces[orientation.RED].tiles[6],self.faces[orientation.YELLOW].tiles[6] =  self.faces[orientation.YELLOW].tiles[6],self.faces[orientation.RED].tiles[6]
        self.faces[orientation.RED].tiles[11],self.faces[orientation.YELLOW].tiles[11] =  self.faces[orientation.YELLOW].tiles[11],self.faces[orientation.RED].tiles[11]
        self.faces[orientation.RED].tiles[12],self.faces[orientation.YELLOW].tiles[12] =  self.faces[orientation.YELLOW].tiles[12],self.faces[orientation.RED].tiles[12]




    # Perform the l action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Rotates the left corner piece.
    def l(self):
         self.faces[orientation.RED].tiles[15],self.faces[orientation.GREEN].tiles[9], self.faces[orientation.YELLOW].tiles[15] = self.faces[orientation.YELLOW].tiles[15],self.faces[orientation.RED].tiles[15], self.faces[orientation.GREEN].tiles[9]

    # Perform the l' action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Rotates the left corner piece the opposite way.
    def l_Prime(self):
       self.faces[orientation.YELLOW].tiles[15],self.faces[orientation.RED].tiles[15], self.faces[orientation.GREEN].tiles[9] =  self.faces[orientation.RED].tiles[15],self.faces[orientation.GREEN].tiles[9], self.faces[orientation.YELLOW].tiles[15] 

 
    def R(self):
        
        
        self.faces[orientation.YELLOW].tiles[11] , self.faces[orientation.GREEN].tiles[8] = self.faces[orientation.GREEN].tiles[8], self.faces[orientation.YELLOW].tiles[11]
        self.faces[orientation.YELLOW].tiles[4] , self.faces[orientation.GREEN].tiles[13] = self.faces[orientation.GREEN].tiles[13], self.faces[orientation.YELLOW].tiles[4]
        self.faces[orientation.YELLOW].tiles[10] , self.faces[orientation.GREEN].tiles[14] = self.faces[orientation.GREEN].tiles[14], self.faces[orientation.YELLOW].tiles[10]
        
        self.faces[orientation.BLUE].tiles[4] , self.faces[orientation.YELLOW].tiles[4] = self.faces[orientation.YELLOW].tiles[4], self.faces[orientation.BLUE].tiles[4]
        self.faces[orientation.BLUE].tiles[10] , self.faces[orientation.YELLOW].tiles[10] = self.faces[orientation.YELLOW].tiles[10], self.faces[orientation.BLUE].tiles[10]
        self.faces[orientation.BLUE].tiles[11] , self.faces[orientation.YELLOW].tiles[11] = self.faces[orientation.YELLOW].tiles[11], self.faces[orientation.BLUE].tiles[11]
        
        self.r()
    def Rw(self):

        self.R()

        self.faces[orientation.GREEN].tiles[3],  self.faces[orientation.YELLOW].tiles[1] = self.faces[orientation.YELLOW].tiles[1] , self.faces[orientation.GREEN].tiles[3]
        self.faces[orientation.GREEN].tiles[7],  self.faces[orientation.YELLOW].tiles[5] = self.faces[orientation.YELLOW].tiles[5] , self.faces[orientation.GREEN].tiles[7]
        self.faces[orientation.GREEN].tiles[6],  self.faces[orientation.YELLOW].tiles[6]  = self.faces[orientation.YELLOW].tiles[6]  , self.faces[orientation.GREEN].tiles[6]
        self.faces[orientation.GREEN].tiles[11], self.faces[orientation.YELLOW].tiles[12]  = self.faces[orientation.YELLOW].tiles[12]  , self.faces[orientation.GREEN].tiles[11]
        self.faces[orientation.GREEN].tiles[12], self.faces[orientation.YELLOW].tiles[13]  = self.faces[orientation.YELLOW].tiles[13]  , self.faces[orientation.GREEN].tiles[12]

        self.faces[orientation.BLUE].tiles[1],self.faces[orientation.YELLOW].tiles[1] =  self.faces[orientation.YELLOW].tiles[1],self.faces[orientation.BLUE].tiles[1]
        self.faces[orientation.BLUE].tiles[5],self.faces[orientation.YELLOW].tiles[5] =  self.faces[orientation.YELLOW].tiles[5],self.faces[orientation.BLUE].tiles[5]
        self.faces[orientation.BLUE].tiles[6],self.faces[orientation.YELLOW].tiles[6] =  self.faces[orientation.YELLOW].tiles[6],self.faces[orientation.BLUE].tiles[6]
        self.faces[orientation.BLUE].tiles[12],self.faces[orientation.YELLOW].tiles[12] =  self.faces[orientation.YELLOW].tiles[12],self.faces[orientation.BLUE].tiles[12]
        self.faces[orientation.BLUE].tiles[13],self.faces[orientation.YELLOW].tiles[13] =  self.faces[orientation.YELLOW].tiles[13],self.faces[orientation.BLUE].tiles[13]
    def Rw_Prime(self):

        self.Rw()
        self.Rw()

    # Perform the R' action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; Rotates the right tripiece roughly from the front the opposite direction.
    def R_Prime(self):
        self.R()
        self.R()

    # Perform the r action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; rotates the right corner piece.
    def r(self):
        self.faces[orientation.YELLOW].tiles[9],self.faces[orientation.GREEN].tiles[15], self.faces[orientation.BLUE].tiles[9]  = self.faces[orientation.BLUE].tiles[9], self.faces[orientation.YELLOW].tiles[9], self.faces[orientation.GREEN].tiles[15]
    
    #Perform the r' action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; rotates the right corner piece the opposite direction.
    def r_Prime(self):
        self.faces[orientation.YELLOW].tiles[9],self.faces[orientation.GREEN].tiles[15], self.faces[orientation.BLUE].tiles[9] = self.faces[orientation.GREEN].tiles[15],self.faces[orientation.BLUE].tiles[9], self.faces[orientation.YELLOW].tiles[9] 
    
    # perform the b action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; rotates the back corner piece.
    def b(self):
        self.faces[orientation.YELLOW].tiles[0],self.faces[orientation.BLUE].tiles[15] = self.faces[orientation.BLUE].tiles[15], self.faces[orientation.YELLOW].tiles[0]
        self.faces[orientation.RED].tiles[9], self.faces[orientation.YELLOW].tiles[0] = self.faces[orientation.YELLOW].tiles[0] , self.faces[orientation.RED].tiles[9]
        
    # Perform the B action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; rotates the Back corner.
    def B(self):
        self.faces[orientation.YELLOW].tiles[0],self.faces[orientation.BLUE].tiles[15] = self.faces[orientation.BLUE].tiles[15], self.faces[orientation.YELLOW].tiles[0]
        self.faces[orientation.YELLOW].tiles[1],self.faces[orientation.BLUE].tiles[8]  = self.faces[orientation.BLUE].tiles[8],  self.faces[orientation.YELLOW].tiles[1]
        self.faces[orientation.YELLOW].tiles[2],self.faces[orientation.BLUE].tiles[14] = self.faces[orientation.BLUE].tiles[14], self.faces[orientation.YELLOW].tiles[2]
        self.faces[orientation.YELLOW].tiles[3],self.faces[orientation.BLUE].tiles[13] = self.faces[orientation.BLUE].tiles[13], self.faces[orientation.YELLOW].tiles[3]
        
        self.faces[orientation.RED].tiles[4],  self.faces[orientation.YELLOW].tiles[3] = self.faces[orientation.YELLOW].tiles[3] , self.faces[orientation.RED].tiles[4]
        self.faces[orientation.RED].tiles[9], self.faces[orientation.YELLOW].tiles[0] = self.faces[orientation.YELLOW].tiles[0] , self.faces[orientation.RED].tiles[9]
        self.faces[orientation.RED].tiles[10], self.faces[orientation.YELLOW].tiles[2] = self.faces[orientation.YELLOW].tiles[2] , self.faces[orientation.RED].tiles[10]
        self.faces[orientation.RED].tiles[11], self.faces[orientation.YELLOW].tiles[1] = self.faces[orientation.YELLOW].tiles[1] , self.faces[orientation.RED].tiles[11]
    
    # Performs the Bw action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; rotates the Back corner the opposite way.
    def Bw(self):

        self.B()

        self.faces[orientation.YELLOW].tiles[4],self.faces[orientation.BLUE].tiles[3] = self.faces[orientation.BLUE].tiles[3], self.faces[orientation.YELLOW].tiles[4]
        self.faces[orientation.YELLOW].tiles[5],self.faces[orientation.BLUE].tiles[7] = self.faces[orientation.BLUE].tiles[7], self.faces[orientation.YELLOW].tiles[5]
        self.faces[orientation.YELLOW].tiles[6],self.faces[orientation.BLUE].tiles[6] = self.faces[orientation.BLUE].tiles[6], self.faces[orientation.YELLOW].tiles[6]
        self.faces[orientation.YELLOW].tiles[7],self.faces[orientation.BLUE].tiles[12] = self.faces[orientation.BLUE].tiles[12], self.faces[orientation.YELLOW].tiles[7]
        self.faces[orientation.YELLOW].tiles[8],self.faces[orientation.BLUE].tiles[11] = self.faces[orientation.BLUE].tiles[11], self.faces[orientation.YELLOW].tiles[8]

        self.faces[orientation.YELLOW].tiles[4], self.faces[orientation.RED].tiles[1]  = self.faces[orientation.RED].tiles[1] , self.faces[orientation.YELLOW].tiles[4]
        self.faces[orientation.YELLOW].tiles[5], self.faces[orientation.RED].tiles[5]  = self.faces[orientation.RED].tiles[5] , self.faces[orientation.YELLOW].tiles[5]
        self.faces[orientation.YELLOW].tiles[6], self.faces[orientation.RED].tiles[6]  = self.faces[orientation.RED].tiles[6] , self.faces[orientation.YELLOW].tiles[6]
        self.faces[orientation.YELLOW].tiles[7], self.faces[orientation.RED].tiles[12]  = self.faces[orientation.RED].tiles[12] , self.faces[orientation.YELLOW].tiles[7]
        self.faces[orientation.YELLOW].tiles[8], self.faces[orientation.RED].tiles[13]  = self.faces[orientation.RED].tiles[13] , self.faces[orientation.YELLOW].tiles[8]
        
    # Perform the B' action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; rotates the Back corner the opposite way.
    def B_Prime(self):
       self.B()
       self.B()  

    # Perform the Bw' action # https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php as demonstrated here; rotates the Back corner widely the opposite way.
    def Bw_Prime(self):
        self.Bw()
        self.Bw()

    def b_prime(self):
        self.b()
        self.b()
    
    # Displays the faces of the Pyraminx like https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php
    def display_faces(self):
        for i in range(3):
            face = ""
            face = "   " + helper_Print(self.faces[i].tiles[0]) + "   "
            face = face + "\n" + "  " + helper_Print(self.faces[i].tiles[1]) + helper_Print(self.faces[i].tiles[2]) + helper_Print(self.faces[i].tiles[3]) + "  "
            face = face + "\n" + " " + helper_Print(self.faces[i].tiles[4]) + helper_Print(self.faces[i].tiles[5]) + helper_Print(self.faces[i].tiles[6]) + helper_Print(self.faces[i].tiles[7]) + helper_Print(self.faces[i].tiles[8]) + " "
            face = face + "\n"  + helper_Print(self.faces[i].tiles[9]) + helper_Print(self.faces[i].tiles[10]) + helper_Print(self.faces[i].tiles[11]) + helper_Print(self.faces[i].tiles[12]) + helper_Print(self.faces[i].tiles[13]) + helper_Print(self.faces[i].tiles[14]) + helper_Print(self.faces[i].tiles[15])  
            print(face)
            print(Style.RESET_ALL)
        
        face = "" + Style.RESET_ALL
        face = face + helper_Print(self.faces[3].tiles[15]) + helper_Print(self.faces[3].tiles[14]) + helper_Print(self.faces[3].tiles[13]) + helper_Print(self.faces[3].tiles[12]) + helper_Print(self.faces[3].tiles[11]) + helper_Print(self.faces[3].tiles[10]) + helper_Print(self.faces[3].tiles[9])  
        face = face + "\n" + " " + helper_Print(self.faces[3].tiles[8]) + helper_Print(self.faces[3].tiles[7]) + helper_Print(self.faces[3].tiles[6]) + helper_Print(self.faces[3].tiles[5]) + helper_Print(self.faces[3].tiles[4]) + " "
        face = face + "\n" + "  " + helper_Print(self.faces[3].tiles[3]) + helper_Print(self.faces[3].tiles[2]) + helper_Print(self.faces[3].tiles[1]) + "  "
        face = face + "\n" + "   " + helper_Print(self.faces[3].tiles[0]) + "   "
        print(face)
        print(Style.RESET_ALL)
       
    # match_input matches the input of the several available operations.
    def match_input(self, moveInput: str):
        if moveInput == "R":
            self.R()
        if moveInput == "L":
            self.L()
        if moveInput == "U":
            self.U()
        if moveInput == "B":
            self.B()
        if moveInput == "r":
           self.r()
        if moveInput == "l":
            self.l()
        if moveInput == "u":
            self.u()
        if moveInput == "b":
            self.b()
        if moveInput == "R'":
            self.R_Prime()
        if moveInput == "L'":
            self.L_Prime()
        if moveInput == "U'":
            self.U_Prime()
        if moveInput == "B'":
            self.B_Prime()
        if moveInput == "r'":
           self.r_Prime()
        if moveInput == "l'":
            self.l_Prime()
        if moveInput == "u'":
            self.u_Prime()
        if moveInput == "b'":
            self.b_prime()
        if moveInput == "Rw":
            self.Rw()
        if moveInput == "Lw":
            self.Lw()
        if moveInput == "Uw":
            self.Uw()
        if moveInput == "Bw":
            self.Bw()
        if moveInput == "Rw'":
            self.Rw_Prime()
        if moveInput == "Lw'":
            self.Lw_Prime()
        if moveInput == "Uw'":
            self.Uw_Prime()
        if moveInput == "Bw'":   
            self.Bw_Prime()

    # DeepEqual capability. This is performance intensive and memory intensive so avoid this if possible.
    def __eq__ (self, other):
        return self == other

    def randomize(self):
        
        print()
        print("Input a number of moves to make(I recommend less than 10 million, highly recommend less than 1m, as 10m is very slow): ")
        numMoves = "";
        try:
            numMoves = int(input())
        except:
            numMoves = 0
            print("invalid input, please try again using a decimal number please")
        for i in range(numMoves):
            
            moveInput = random.randint(0,24)

            if moveInput == 0:
                self.R()
            if moveInput == 1:
                self.L()
            if moveInput == 2:
                self.U()
            if moveInput == 3:
                self.B()
            if moveInput == 4:
                self.r()
            if moveInput == 5:
                self.l()
            if moveInput == 6:
                self.u()
            if moveInput == 7:
                self.b()
            if moveInput == 8:
                self.R_Prime()
            if moveInput == 9:
                self.L_Prime()
            if moveInput == 10:
                self.U_Prime()
            if moveInput == 11:
                self.B_Prime()
            if moveInput == 12:
                self.r_Prime()
            if moveInput == 13:
                self.l_Prime()
            if moveInput == 14:
                self.u_Prime()
            if moveInput == 15:
                self.B_Prime()
            if moveInput == 16:
                self.Rw()
            if moveInput == 17:
                self.Lw()
            if moveInput == 18:
                self.Uw()
            if moveInput == 19:
                self.Bw()
            if moveInput == 20:
                self.Rw_Prime()
            if moveInput == 21:
                self.Lw_Prime()
            if moveInput == 22:
                self.Uw_Prime()
            if moveInput == 23:   
                self.Bw_Prime()

def helper_Print(tile)-> str:
    face = ""
    if tile.color == "red":
        face = face + Fore.RED + asciiCache.cache[tile.uuid]
    if tile.color == "blue":          
        face = face + Fore.BLUE + asciiCache.cache[tile.uuid]
    if tile.color == "yellow":
        face = face + Fore.LIGHTYELLOW_EX  + asciiCache.cache[tile.uuid] 
    if tile.color == "green":
        face = face + Fore.GREEN  + asciiCache.cache[tile.uuid]
    face + Style.RESET_ALL
    return face

