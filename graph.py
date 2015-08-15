import numpy as np

from corner import Corner

class Graph():

    def __init__(self, lines):
        self.lines = lines
        self.corners = []
        self.horizon_lines = []
        self.vertical_lines = []

    def set_directed_lines(self):
        for line in self.lines:
            if line.direction is 'h':
                self.horizon_lines.append(line)
            else:
                self.vertical_lines.append(line)

    def make_graph(self):
        self.set_directed_lines()

        for h_line in self.horizon_lines:
            coeff_x, coeff_y, bias = h_line.eq
            for v_line in self.vertical_lines:
                cx, cy, b = v_line.eq
                A = np.array([[coeff_x, coeff_y], [cx, cy]])
                B = np.array([bias, b])
                root = Corner(np.linalg.solve(A, B))
                h_line.corners.append(root)
                v_line.corners.append(root)

        for line in self.lines:
            line.line_link()
            self.corners += line.corners
