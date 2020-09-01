from string import ascii_lowercase
#Global ascii map
class asciiCache():
    def __init__(self):
        self.cache = {}
        count = 0
        for i in ascii_lowercase:
            self.cache[count] = i
            count +=1
        del(count) 