
import math
import copy
import Tree
import heapq
import pyraminx
import solver

#In progress
def test_testSolver():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.l()
    
    testAlgorithm = Tree.node(testPyraminx, 0, 0)

    solver.solver(testAlgorithm)
    assert(testAlgorithm.pointers[0].moveToGetHere == "l")


