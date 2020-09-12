
import math
import copy
import pyraminx
#In progress
class node:
    def __init__(self, Pyraminx, NodeUUID, parentHeuristic):
        self.Pyraminx = Pyraminx
        self.pointers = []

        self.parent = None
        self.moveToGetHere = "Initial"

        self.UUID = NodeUUID

        self.generate_heuristic(parentHeuristic)
        self.determine_validity()

        if self.UUID == 0:
            pass

    def generate_heuristic(self, parentHeuristic):
        self.heuristic = parentHeuristic + 1

    def determine_validity(self):
        Test = pyraminx.pyraminx()
        checker = 1
        for face in range(4):
            for tile in range(16):
                if Test.faces[face].tiles[tile].color != self.Pyraminx.faces[face].tiles[tile].color:
                    checker = 0
      
        
    def expand(self):
        if self.pointers:
            return


        Child = pyraminx.pyraminx()
        for i in range(4):
            Node = None
            if i == 0:
                Child.l()
                Node = node(Child, i + self.UUID, self.heuristic)
                Node.moveToGetHere = "l"
                Node.parent = self
            if i == 1:
                Child.r()
                Node = node(Child, i + self.UUID, self.heuristic)
                Node.moveToGetHere = "r"
                Node.parent = self
            if i == 2:
                Child.b()
                Node = node(Child, i + self.UUID, self.heuristic)
                Node.moveToGetHere = "b"
                Node.parent = self
            if i == 3:
                Child.u()
                Node = node(Child, i + self.UUID, self.heuristic)
                Node.moveToGetHere = "u"
                Node.parent = self

            self.pointers.append(copy.deepcopy(Node))
