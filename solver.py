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
            currentNode.determine_validity()
            if currentNode.heuristic == 0:
                self.solved()
                print("lmao")
                break

            currentNode.expand()
            for childNode in currentNode.pointers:
                heapq.heappush(self.heap, childNode)
            

    def solved(self):
        print("")
        exit()