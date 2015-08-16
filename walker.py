
class Walker():

    def __init__(self, root, direction, graph):
        self.root = root
        self.direction = direction
        self.current_corner = root
        self.quad_list = [root]
        self.graph = graph

        if root is None:
            return
        self.start()

    def start(self):
        def when_up():
            self.current_corner = self.root.up
            self.turn_left()
            self.turn_right()
            self.graph.start_walker(Walker(self.root.up, 'up', self.graph))

        def when_down():
            self.current_corner = self.current_corner.down

        def when_left():
            self.current_corner = self.current_corner.left

        def when_right():
            self.current_corner = self.current_corner.right

        return {
            'up': when_up,
            'down': when_down,
            'right': when_right,
            'left': when_left
        }[self.direction]()

    def turn_left(self):
        return

    def turn_right(self):
        return