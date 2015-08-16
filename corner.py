

class Corner():

    def __init__(self, corner):
        self.corner = corner
        self.x, self.y = self.corner
        self.up = None
        self.right = None
        self.down = None
        self.left = None

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)