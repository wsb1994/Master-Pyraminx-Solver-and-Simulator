import pyraminx
import Tree
import sys


def test_heuristic():
    testPyraminx = pyraminx.pyraminx()
    testAlgorithm =Tree.node(testPyraminx, 0,0)
    testAlgorithm.determine_validity()
    
    assert(testAlgorithm.heuristic == 0)
    testPyraminx.B()
    testPyraminx.Rw_Prime()
    testPyraminx.L_Prime()
    
    
    testAlgorithm = Tree.node(testPyraminx, 0, 0)
    testAlgorithm.expand()
    testAlgorithm.expand()

    assert(testAlgorithm.pointers[0].moveToGetHere == "l")

