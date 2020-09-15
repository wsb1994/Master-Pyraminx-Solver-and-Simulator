
import math
import copy
import Tree
import heapq
import pyraminx
import solver

#In progress
def test_testSolver():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.l_Prime()
    testPyraminx.r_Prime()
    testPyraminx.b_Prime()
    testPyraminx.u_Prime()
    
    testAlgorithm = Tree.node(testPyraminx, 0)

    solver.solver(testAlgorithm)
    


