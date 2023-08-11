from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2, fill_color="black"):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        from_cell_center_x = (self._x1 + self._x2) // 2
        from_cell_center_y = (self._y1 + self._y2) // 2
        to_cell_center_x = (to_cell._x1 + to_cell._x2) // 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) // 2
        if undo:
            self._win.draw_line(Line(Point(from_cell_center_x, from_cell_center_y),
                                Point(to_cell_center_x, to_cell_center_y)), "gray")
        else:
            self._win.draw_line(Line(Point(from_cell_center_x, from_cell_center_y),
                                Point(to_cell_center_x, to_cell_center_y)), "red")
                