import numpy as np

from skimage.color import rgb2gray


class Image():
    def __init__(self, img, config=None):
        self.img = img
        self.config = config
        self.gray_img = rgb2gray(self.img)
        self.blurred_img = []
        self.edges = []
        self.lines = []
        self.line_images = []
        self.rectangles = []

        self.edge_config = None
        self.blur_config = None
        self.line_config = None

        self.is_blur = False
        self.is_edge = False
        self.is_line = False
        self.is_graph = False

        if config is not None:
            self.set_config()

    def set_config(self):
        if 'edge_config' in self.config:
            self.edge_config = self.config['edge_config']
        if 'blur_config' in self.config:
            self.blur_config = self.config['blur_config']
        if 'line_config' in self.config:
            self.line_config = self.config['line_config']

    def set_blurred_img(self):
        from scipy import ndimage as ndi

        if self.blur_config is not None:
            self.blurred_img = ndi.gaussian_filter(self.gray_img, **self.blur_config)
        else:
            self.blurred_img = ndi.gaussian_filter(self.gray_img, sigma=5)

        self.is_blur = True

    def set_edges(self):

        if not self.is_blur:
            self.set_blurred_img()

        from skimage.feature import canny

        if self.edge_config is not None:
            self.edges = canny(self.blurred_img, **self.edge_config)
        else:
            self.edges = canny(self.blurred_img, sigma=2)

        self.is_edge = True

    def set_lines(self):

        if not self.is_edge:
            self.set_edges()

        from skimage.transform import hough_line, hough_line_peaks
        from line import Line

        h, theta, d = hough_line(self.edges)

        for _, angle, dist in zip(*hough_line_peaks(h, theta, d, threshold=100)):
            cosine = np.cos(angle)
            sine = np.sin(angle)

            if np.abs(sine) > np.sin(np.pi / 4):
                newline = Line([cosine, sine, dist], 'h')
            else:
                newline = Line([cosine, sine, dist], 'v')
            self.lines.append(newline)

        self.is_line = True

    def set_graph(self):

        if not self.is_line:
            self.set_lines()

        from graph import Graph

        graph = Graph(self.lines)
        self.rectangles = graph.get_quad_list()

        self.is_graph = True

    def get_rectangles(self):

        if not self.is_graph:
            self.set_graph()

        return self.rectangles

    def polygon_area(self, corners):
        n = len(corners)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += corners[i].corner[0] * corners[j].corner[1]
            area -= corners[j].corner[0] * corners[i].corner[1]
        area = abs(area) / 2.0
        return area

    def get_poly_coords(self):
        if not self.is_graph:
            self.set_graph()

        y_coords = map(lambda x: map(lambda y: y.corner[1], x), self.rectangles)
        x_coords = map(lambda x: map(lambda y: y.corner[0], x), self.rectangles)
        return zip(y_coords, x_coords)

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


















