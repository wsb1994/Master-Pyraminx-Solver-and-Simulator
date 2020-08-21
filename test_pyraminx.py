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
    testPyraminx = pyraminx.pyraminx()
    

    testPyraminx.faces[pyraminx.orientation.GREEN].tiles[1].color = "warm"
    testPyraminx.faces[pyraminx.orientation.GREEN].tiles[6].color = "warmer"
    testPyraminx.faces[pyraminx.orientation.GREEN].tiles[7].color = "warmier"
    testPyraminx.faces[pyraminx.orientation.GREEN].tiles[4].color = "warmiest"

    testPyraminx.L()
    
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[6].color == "warm"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[3].color =="warmer"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[7].color == "warmier"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[8].color == "warmiest"

def test_L_Prime():
    testPyraminx = pyraminx.pyraminx()
    

    testPyraminx.faces[pyraminx.orientation.RED].tiles[6].color = "warm"
    testPyraminx.faces[pyraminx.orientation.RED].tiles[3].color = "warmer"
    testPyraminx.faces[pyraminx.orientation.RED].tiles[7].color = "warmier"
    testPyraminx.faces[pyraminx.orientation.RED].tiles[8].color = "warmiest"

    testPyraminx.L_Prime()
    
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[1].color == "warm"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[6].color =="warmer"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[7].color == "warmier"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[4].color == "warmiest"



def test_l():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.l()

    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[8].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[4].color == "red"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[8].color == "green"



def test_lPrime():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.l_Prime()

    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[8].color == "green"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[4].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[8].color == "red"


def test_R():
    testPyraminx = pyraminx.pyraminx()
    

    testPyraminx.faces[pyraminx.orientation.BLUE].tiles[1].color = "warm"
    testPyraminx.faces[pyraminx.orientation.BLUE].tiles[4].color = "warmer"
    testPyraminx.faces[pyraminx.orientation.BLUE].tiles[5].color = "warmier"
    testPyraminx.faces[pyraminx.orientation.BLUE].tiles[6].color = "warmiest"
    testPyraminx.R()
    
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[1].color == "warm"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[4].color =="warmer"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[5].color == "warmier"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[6].color == "warmiest"

def test_RPrime():
    testPyraminx = pyraminx.pyraminx()
    

    testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[1].color = "warm"
    testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[4].color = "warmer"
    testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[5].color = "warmier"
    testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[6].color = "warmiest"
    testPyraminx.R_Prime()
    
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[1].color == "warm"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[4].color =="warmer"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[5].color == "warmier"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[6].color == "warmiest"


def test_r():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.r()

    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[8].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[4].color =="blue"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[4].color == "green"


def test_rPrime():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.r_Prime()

    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[8].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[4].color =="green"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[4].color == "yellow"


def test_B():
    pass


def test_BPrime():
    pass


def test_b():
    pass


def test_bPrime():
    pass
