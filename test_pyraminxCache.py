import pyraminx as pyraminx
import copy as copy
import pyraminxCache as Cache

def test_cache():
    testPyraminx = pyraminx.pyraminx()
    

    testPyraminx.faces[pyraminx.orientation.GREEN].tiles[1].color = "warm"

    testPyraminx.L()

    testCache = Cache.pyraminxCache()
    testCache.encache(testPyraminx)
    testCache.encache(testPyraminx)
    testCache.encache(testPyraminx)

    for i in testCache.cache:
        assert i == testPyraminx

    print("")