import pyraminx
import Tree
import sys


def test_heuristic():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.B()
    testPyraminx.Rw_Prime()
    testPyraminx.L_Prime()
    
    testAlgorithm = Tree.node(testPyraminx, 0, 0)
    testAlgorithm.expand()
    testAlgorithm.expand()
    testAlgorithm.Pyraminx.display_faces()

