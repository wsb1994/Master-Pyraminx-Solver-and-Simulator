import pyraminx as pyraminx
import copy as copy



def test_u():
    testMinx = pyraminx.pyraminx()
    testMinx.u()

    assert testMinx.faces[pyraminx.orientation.RED].tiles[0].color == "green" 




def test_uPrime():
    testMinx = pyraminx.pyraminx()
    testMinx.u_Prime()

    assert testMinx.faces[pyraminx.orientation.RED].tiles[0].color == "blue" 


def test_U():
    testMinx = pyraminx.pyraminx()
    testMinx.U()

    for i in range(4):
        assert testMinx.faces[pyraminx.orientation.RED].tiles[i].color == "green" 


def test_UPrime():
    testMinx = pyraminx.pyraminx()
    testMinx.U_Prime()
    
    for i in range(4):
        assert testMinx.faces[pyraminx.orientation.RED].tiles[i].color == "blue" 



def test_L():
    pass


def test_LPrime():
    pass


def test_l():
    pass


def test_lPrime():
    pass


def test_R():
    pass


def test_RPrime():
    pass


def test_r():
    pass


def test_rPrime():
    pass


def test_B():
    pass


def test_BPrime():
    pass


def test_b():
    pass


def test_bPrime():
    pass
