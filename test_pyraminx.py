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

def test_Uw():
    testMinx = pyraminx.pyraminx()
    testMinx.Uw()

    for i in range(9):
        assert testMinx.faces[pyraminx.orientation.RED].tiles[i].color == "green" 

def test_Uw_Prime():
    testMinx = pyraminx.pyraminx()
    testMinx.Uw_Prime()
    
    for i in range(9):
        assert testMinx.faces[pyraminx.orientation.RED].tiles[i].color == "blue" 

def test_L():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.L()
   

    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[8].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[13].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[14].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[15].color == "yellow"

def test_LW():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.Lw_Prime()

    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[4].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[9].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[10].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[11].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[1].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[5].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[6].color == "yellow"

def test_LW_Prime():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.Lw_Prime()
    

    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[4].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[9].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[10].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[11].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[1].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[5].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[6].color == "yellow"
      
def test_L_Prime():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.L_Prime()
    

    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[4].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[9].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[10].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[11].color == "yellow"

def test_l():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.l()

    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[15].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[9].color == "red"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[15].color == "green"

def test_lPrime():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.l_Prime()
    testPyraminx.l_Prime()

    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[15].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[9].color == "red"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[15].color == "green"

def test_R():
    testPyraminx = pyraminx.pyraminx()
    
    testPyraminx.R()
    
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[4].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[9].color =="blue"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[10].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[11].color == "blue"

def test_RPrime():
    testPyraminx = pyraminx.pyraminx()
    referencePyraminx = pyraminx.pyraminx()

    referencePyraminx.R_Prime()
    testPyraminx.R()
    testPyraminx.R()

    for i in range (4):
        for j in range(16):
            assert testPyraminx.faces[i].tiles[j].color == referencePyraminx.faces[i].tiles[j].color

def test_r():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.r()

    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[15].color == "yellow"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[9].color =="blue"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[9].color == "green"

def test_rPrime():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.r_Prime()

    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[15].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[9].color =="green"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[9].color == "yellow"

    testPyraminx.r()

    assert testPyraminx.faces[pyraminx.orientation.GREEN].tiles[8].color == "green"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[4].color =="yellow"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[4].color == "blue"

def test_B():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.B()

    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[4].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[9].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[10].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.RED].tiles[11].color == "blue"

def test_Bw():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.B()
    testPyraminx.Bw()

    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[0].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[1].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[2].color == "blue"
    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[3  ].color == "blue"

def test_BPrime():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.B_Prime()

    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[8].color == "red"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[13].color == "red"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[14].color == "red"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[15].color == "red"

def test_Bw_Prime():
    testPyraminx = pyraminx.pyraminx()
    testPyraminx.Bw_Prime()

    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[3].color == "red"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[11].color == "red"
    assert testPyraminx.faces[pyraminx.orientation.BLUE].tiles[15].color == "red"
    

def test_b():
    testPyraminx = pyraminx.pyraminx()

    testPyraminx.b()
    

    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[0].color == "red"


def test_bPrime():
    testPyraminx = pyraminx.pyraminx()

    
    testPyraminx.b_prime()

    assert testPyraminx.faces[pyraminx.orientation.YELLOW].tiles[0].color == "blue"