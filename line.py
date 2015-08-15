


class Line():

    def __init__(self, eq, direction):
        self.eq = eq
        self.corners = []
        self.direction = direction

    def line_link(self):
        if self.direction is 'h':
            self.corners = sorted(self.corners, key=lambda corner: corner.x)
            for l, r in zip(self.corners[:-1], self.corners[1:]):
                l.right = r
                r.left = l
        else:
            self.corners = sorted(self.corners, key=lambda corner: corner.y)
            for d, u in zip(self.corners[:-1], self.corners[1:]):
                u.down = d
                d.up = u