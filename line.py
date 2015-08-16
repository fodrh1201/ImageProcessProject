


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

    # def draw_lines(self):
    #
    #     self.set_equations()
    #
    #     from skimage.draw import line
    #
    #     def get_line(lines):
    #         def sub_getline(eq):
    #             coeff_x, coeff_y, bias = eq
    #             sim_eq_A = [np.array([[coeff_x, coeff_y], [cx, cy]]) for cx, cy, cb in lines]
    #             sim_eq_B = [np.array([bias, cb]) for cx, cy, cb in lines]
    #             return [np.linalg.solve(a, b).astype(int) for a, b in zip(sim_eq_A, sim_eq_B)]
    #
    #         return sub_getline
    #
    #     def drawline(points):
    #         start, end = points
    #         rr, cc = line(start[1], start[0], end[1], end[0])
    #         line_image[rr, cc] = 1
    #
    #     rows, cols = self.gray_img.shape
    #     line_image = np.zeros((rows + 1, cols + 1), dtype=np.uint8)
    #     equations_horizon, equations_vertical = self.line_equations
    #     vertical_lines = [[1, 0, 0], [1, 0, cols - 1]]
    #     horizon_lines = [[0, 1, 0], [0, 1, rows - 1]]
    #     h_points = map(get_line(vertical_lines), equations_horizon)
    #     v_points = map(get_line(horizon_lines), equations_vertical)
    #
    #     for points in h_points + v_points:
    #         drawline(points)
    #
    #     self.line_images = line_image