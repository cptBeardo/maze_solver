from creation import Line, Point

class Cell():
    def __init__(self, win=None):
        self._win = win
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
        
        # DEBUGGING: if self._win:
        # DEBUGGING:     canvas = self._win.get_canvas()

        # DEBUGGING:     """left wall creation"""
        # DEBUGGING:     p1 = Point(self._x1, self._y1)
        # DEBUGGING:     p2 = Point(self._x1, self._y2)
        # DEBUGGING:     left_wall = Line(p1, p2)
        # DEBUGGING:     if self.has_left_wall:
        # DEBUGGING:         left_wall.draw(canvas, fill_color="black")
        # DEBUGGING:     else:
        # DEBUGGING:         left_wall.draw(canvas, fill_color="#d9d9d9")
            

        # DEBUGGING:     """right wall creation"""
        # DEBUGGING:     p1 = Point(self._x2, self._y1)
        # DEBUGGING:     p2 = Point(self._x2, self._y2)
        # DEBUGGING:     right_wall = Line(p1, p2)
        # DEBUGGING:     if self.has_right_wall:
        # DEBUGGING:         right_wall.draw(canvas, fill_color="black")
        # DEBUGGING:     else:
        # DEBUGGING:         right_wall.draw(canvas, fill_color="#d9d9d9")

        # DEBUGGING:     """top wall creation"""    
        # DEBUGGING:     p1 = Point(self._x1, self._y1)
        # DEBUGGING:     p2 = Point(self._x2, self._y1)
        # DEBUGGING:     top_wall = Line(p1, p2)
        # DEBUGGING:     if self.has_top_wall:
        # DEBUGGING:         top_wall.draw(canvas, fill_color="black")
        # DEBUGGING:     else:
        # DEBUGGING:         top_wall.draw(canvas, fill_color="#d9d9d9")

        # DEBUGGING:     """bottom wall creation"""
        # DEBUGGING:     p1 = Point(self._x1, self._y2)
        # DEBUGGING:     p2 = Point(self._x2, self._y2)
        # DEBUGGING:     bottom_wall = Line(p1, p2)
        # DEBUGGING:     if self.has_bottom_wall:
        # DEBUGGING:         bottom_wall.draw(canvas, fill_color="black")
        # DEBUGGING:     else:
        # DEBUGGING:         bottom_wall.draw(canvas, fill_color="#d9d9d9")

    # DEBUGGING: def get_center(self):
    # DEBUGGING:     center_x = (self._x1 + self._x2) / 2
    # DEBUGGING:     center_y = (self._y1 + self._y2) / 2
    # DEBUGGING:     return (center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_lenght2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_lenght2 + to_cell._x1
        y_center2 = half_lenght2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)

        # DEBUGGING: from_center = self.get_center()
        # DEBUGGING: to_center = to_cell.get_center()

        # DEBUGGING: from_point = Point(from_center[0], from_center[1])
        # DEBUGGING: to_point = Point(to_center[0], to_center[1])

        # DEBUGGING: line = Line(from_point, to_point)


        # DEBUGGING: color = "gray" if undo else "red"
        # DEBUGGING: self._win.draw_line(line, color)
