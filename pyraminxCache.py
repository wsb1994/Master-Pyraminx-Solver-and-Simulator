
class pyraminxCache:

    def __init__(self):
        self.cache = []
    
    def encache(self, cacheItem):
        self.cache.append(cacheItem)

    def clear(self):
        self.cache = []