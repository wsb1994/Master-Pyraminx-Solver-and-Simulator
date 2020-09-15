import math
import copy
import Tree
import heapq

class solver:
    def __init__(self, node):
        self.heap = []
        self.bigCount = 0
        self.path = []

        heapq.heappush(self.heap, node)

        while self.heap:
            currentNode = heapq.heappop(self.heap)
            currentNode.generate_heuristic()

            if currentNode.check_goal():
                self.solved(currentNode)
                return

            if not currentNode.pointers:
                currentNode.expand()
                self.bigCount += 1
                
                for childNode in currentNode.pointers:
                    childNode.generate_heuristic()
                    childNode.parent = currentNode
                
                    heapq.heappush(self.heap, childNode)
            

    def solved(self, node):
        self.path.append("solved")
        while node != None:
            self.path.append(node.moveToGetHere)
            node = node.parent
        self.heap = []