from tkinter import Tk, BOTH, Canvas
from time import sleep


class Window():
    def __init__(self, width, height):
        self.width = width  # not included in solution file?
        self.height = height  # not included in solution file?
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height) # can have any number of parameters, but must have the master (this case, self.__root)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close) # add after creating redraw(), wait_to_close(), and close() methods

    def get_canvas(self):
        return self.__canvas
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...") # not in my original code, but was in the solution file, so I added it because I like it
    
    def close(self):
        self.__running = False

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self.win, 0, 0, 0, 0))
                self._draw_cell(i, j)
            self._cells.append(column)

    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j] = Cell(self.win, x1, y1, x2, y2)
        self._cells[i][j].draw()

        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05) # if I only import time, I would need to do time.sleep()

class Cell():
    def __init__(self, win, x1, y1, x2, y2):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        

    def draw(self):
        canvas = self._win.get_canvas()

        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            left_wall = Line(p1, p2)
            left_wall.draw(canvas)
        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            right_wall = Line(p1, p2)
            right_wall.draw(canvas)
        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            top_wall = Line(p1, p2)
            top_wall.draw(canvas)
        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            bottom_wall = Line(p1, p2)
            bottom_wall.draw(canvas)

    def get_center(self):
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return (center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        from_center = self.get_center()
        to_center = to_cell.get_center()

        from_point = Point(from_center[0], from_center[1])
        to_point = Point(to_center[0], to_center[1])

        line = Line(from_point, to_point)


        color = "gray" if undo else "red"
        self._win.draw_line(line, color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        x1 = self.point1.x
        y1 = self.point1.y
        x2 = self.point2.x
        y2 = self.point2.y

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
