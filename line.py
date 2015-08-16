


class Line():

    def __init__(self, eq, direction):
        self.eq = eq
        self.corners = []
        self.direction = direction

    def line_link(self):
        n = len(self.corners)
        if self.direction is 'h':
            self.corners = sorted(self.corners, key=lambda corner: corner.x)

            for i in range(n - 1):
                j = 1
                while self.corners[i].x is self.corners[i + j].x:
                    self.corners[i + j].left = self.corners[i]
                    j += 1
                self.corners[i].right = self.corners[i + j]
                self.corners[i + j].left = self.corners[i]
        else:
            self.corners = sorted(self.corners, key=lambda corner: corner.y)

            for i in range(n - 1):
                j = 1
                while self.corners[i].y is self.corners[i + j].y:
                    self.corners[i + j].down = self.corners[i]
                    j += 1
                self.corners[i].up = self.corners[i + j]
                self.corners[i + j].down = self.corners[i]

    # @property
    # def __repr__(self):
    #     return self.eq
    #
    # @property
    # def __str__(self):
    #     return self.eq