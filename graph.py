import numpy as np

from corner import Corner

class Graph():

    def __init__(self, horizon_lines, vertical_lines):
        self.horizon_lines = horizon_lines
        self.vertical_lines = vertical_lines

    def make_graph(self):
        def find_root_with_lines(line_eq, lines):
            coeff_x, coeff_y, bias = line_eq
            A = [np.array([[coeff_x, coeff_y], [cx, cy]]) for cx, cy, cb in lines]
            B = [np.array([bias, cb]) for cx, cy, cb in self.vertical_lines]
            roots = [np.linalg.solve(a, b) for a, b in zip(A, B)]
            return roots

        def make_corners(roots, direction):
            if direction is 'h':
