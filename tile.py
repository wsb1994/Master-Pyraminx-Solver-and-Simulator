
#defines a tile with a color, and an indicator of which tile space it originally occupied on it's original face
class tile:
    def __init__(self, color, uuid):
        self.color= color
        self.uuid = uuid
    
#that's really annoying, you can only swap the individual bits, not the object. That's SO ANNOYING
