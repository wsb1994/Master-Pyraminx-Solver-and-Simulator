
import math
import copy
import pyraminx
#In progress


class node:
    def __init__(self, Pyraminx, NodeUUID, parentHeuristic):
        self.Pyraminx = Pyraminx
        self.pointers = []
        self.heuristic = math.inf
        self.parent = None
        self.moveToGetHere = "Initial"

        self.UUID = NodeUUID

        self.generate_heuristic(parentHeuristic)

        
    def __gt__(self, other):
        if self.heuristic > other.heuristic:
            return True
        return False

    def __lt__(self, other):
        if self.heuristic < other.heuristic:
            return True
        return False
        
    def generate_heuristic(self, parentHeuristic):
        self.heuristic = 1

    def determine_validity(self):
        Test = pyraminx.pyraminx()
        checker = 0
        for face in range(4):
            for tile in range(16):
                if Test.faces[face].tiles[tile].color != self.Pyraminx.faces[face].tiles[tile].color:
                    checker = checker+1
        if checker == 0:
            self.heuristic = 0
      
        
    def expand(self):
        if self.pointers:
            return


        Child = copy.deepcopy(self.Pyraminx)
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
