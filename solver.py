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
                self.solved(currentNode)
                print("lmao")
                break

            currentNode.expand()
            for childNode in currentNode.pointers:
                childNode.determine_validity()
                if childNode.heuristic == 0:
                    self.solved(childNode)
                    print("lmao")
                    break
                heapq.heappush(self.heap, childNode)
            

    def solved(self, node):
        print("")
        ##print parents in order
        exit()