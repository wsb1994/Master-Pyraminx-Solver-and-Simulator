import surface as surface

def test_surfaceGeneration():
    testSurface = surface.surface("green")

    for i in range(9):
        assert testSurface.tiles[i].color == "green"
        assert testSurface.tiles[i].uuid == i
    