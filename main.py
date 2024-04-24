from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from kivy.properties import NumericProperty


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 4
    V_LINES_SPACING = 0.1   # percentage in screen width
    H_NB_LINES = 8
    H_LINES_SPACING = 0.2   # percentage in screen height

    vertical_lines = []
    horizontal_lines = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print("Init W: " + str(self.width) + " Init H: " + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()

    def on_parent(self, widget, parent):
        # print("Parent W: " + str(self.width) + " Parent H: " + str(self.height))
        pass

    def on_size(self, *args):
        print("ON_SIZE W: " + str(self.width) + " H: " + str(self.height))
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()
        self.update_horizontal_lines()

    def on_perspective_point_x(self, widget, value):
        # print("PX: " + str(value))
        pass

    def on_perspective_point_y(self, widget, value):
        # print("PY: " + str(value))
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        center_line_x = int(self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2) + 0.5
        for i in range(0, self.V_NB_LINES):
            line_x = int(center_line_x + offset*spacing)

            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        center_line_x = int(self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2) + 0.5

        xmin = center_line_x + offset*spacing
        xmax = center_line_x - offset*spacing
        spacing_y = self.H_LINES_SPACING * self.height

        for i in range(0, self.H_NB_LINES):
            line_y = i * spacing_y
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_perspective(self, x, y):
        tr_y = y*self.perspective_point_y / self.height
        if tr_y > self.perspective_point_y:
            tr_y = self.perspective_point_y

        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - tr_y
        proportion_y = diff_y / self.perspective_point_y
        tr_x = self.perspective_point_x + diff_x*proportion_y
        return int(tr_x), int(tr_y)


class GalaxyApp(App):
    pass


GalaxyApp().run()
