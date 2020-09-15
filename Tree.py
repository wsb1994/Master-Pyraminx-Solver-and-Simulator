
import math
import copy
import pyraminx as Pyraminx
#In progress


class node:
    def __init__(self, Pyraminx, currentMoveDepth):
        self.Pyraminx = Pyraminx
        self.pointers = []
        self.parent = None
        self.heuristic = math.inf
        self.cost = math.inf
        
        self.moveToGetHere = "Initial"
        self.currentMoveDepth = currentMoveDepth

    
    def __gt__(self, other):
        if self.cost > other.cost:
            return True
        return False

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        return False
        
    def generate_heuristic(self):
        testPyraminx = Pyraminx.pyraminx()
        count = 0
        for face in range(4):
            for tile in range(16):
                if testPyraminx.faces[face].tiles[tile].color != self.Pyraminx.faces[face].tiles[tile].color:
                    count +=1
        result = math.ceil(count/4)
        self.heuristic = result
        self.cost = self.currentMoveDepth + result


    def check_goal(self):
        Test = Pyraminx.pyraminx()
        checker = 0
        for face in range(4):
            for tile in range(16):
                if Test.faces[face].tiles[tile].color != self.Pyraminx.faces[face].tiles[tile].color:
                    checker = checker+1
        if checker == 0:
            return True
        return False
      
        
    def expand(self):
        if self.pointers:
            return


        
        for i in range(12):
            Child = copy.deepcopy(self.Pyraminx)
            Node = None
            if i == 0:
                Child.l()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "l"
             
            if i == 1:
                Child.r()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "r"
            
            if i == 2:
                Child.b()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "b"
              
            if i == 3:
                Child.u()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "u"
            
            if i == 4:
                Child.L()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "L"
             
            if i == 5:
                Child.R()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "R"
            
            if i == 6:
                Child.B()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "B"
              
            if i == 7:
                Child.U()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "Uw"
            
            if i == 8:
                Child.Lw()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "Lw"
             
            if i == 9:
                Child.Rw()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "Rw"
            
            if i == 10:
                Child.Bw()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "Bw"
              
            if i == 11:
                Child.Uw()
                Node = node(Child, 1 + self.currentMoveDepth)
                Node.moveToGetHere = "Uw"

            self.pointers.append(copy.deepcopy(Node))
