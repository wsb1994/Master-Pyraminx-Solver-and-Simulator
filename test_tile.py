import tile as tile
import copy

def test_instantiation():
    testTile = tile.tile("green", 0)

    assert testTile.color == "green"
    assert testTile.uuid == 0


def test_swap():
    reference1 = tile.tile("green",0)
    reference2 = tile.tile("yellow",1)

    tile1 = copy.copy(reference1)
    tile2 = copy.copy(reference2)

    tile.swap_tile(tile1,tile2)

   
    assert tile1.color == reference2.color
    assert tile1.uuid == reference2.uuid

    assert tile2.color == reference1.color
    assert tile2.uuid == reference1.uuid
