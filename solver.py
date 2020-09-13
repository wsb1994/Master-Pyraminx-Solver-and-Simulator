import math
import copy
import Tree
import heapq

class solver:
    def __init__(self, node):
        self.heap = []
        heapq.heappush(self.heap, node)

        while self.heap:
            currentNode = heapq.heappop(self.heap)
            currentNode.generate_heuristic()
           # currentNode.Pyraminx.display_faces()
            if currentNode.check_goal():
                self.solved(currentNode)
                print("lmao")
                return
            if not currentNode.pointers:
                currentNode.expand()
                for childNode in currentNode.pointers:
                    childNode.generate_heuristic()
                    childNode.parent = currentNode
                    heapq.heappush(self.heap, childNode)
            

    def solved(self, node):
        print("solved state")
        while node != None:
            print(node.moveToGetHere)
            node = node.parent
        self.heap = []