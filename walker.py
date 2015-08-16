import copy

class Walker():

    # will make singleton
    def __init__(self, corners):
        self.corners = corners
        self.root = corners[0]
        self.quad_list = []
        self.find_root()
        self.collect_quad_list()


    def find_root(self):
        while self.root.left is not None:
            self.root = self.root.left
        while self.root.down is not None:
            self.root = self.root.down

        print('root', self.root, self.root.right, self.root.right.up, self.root.right.up.left)
        print('root', self.root, self.root.right, self.root.right.up, self.root.up)


    def collect_quad_list(self):
        origin_v = self.root
        while origin_v.up is not None:
            origin_h = copy.deepcopy(origin_v)
            while origin_h.right is not None:
                quad = [origin_h, origin_h.right, origin_h.right.up, origin_h.right.up.left]
                self.quad_list.append(quad)
                origin_h = origin_h.right
            origin_v = origin_v.up

    def get_quad_list(self):
        return self.quad_list
