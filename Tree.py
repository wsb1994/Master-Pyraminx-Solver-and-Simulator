
import math

class node:
    def __init__(self, Pyraminx, NodeUUID):
        self.Pyraminx = Pyraminx
        self.pointers = []
        self.parent = None

        self.UUID = NodeUUID
        self.heuristic = math.inf

        #self.generate_heuristic()
        if self.UUID == 0:
            pass

    def generate_heuristic(self):
        pass
