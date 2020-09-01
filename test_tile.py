import tile as tile
import copy

def test_instantiation():
    testTile = tile.tile("green", 0)

    assert testTile.color == "green"
    assert testTile.uuid == 0
