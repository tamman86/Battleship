class Ship:
    def __init__(self, name, size, orientation):
        self.name = name
        self.size = size
        self.orientation = orientation
        self.sunk = False
        self.health = size
        self.place = []
