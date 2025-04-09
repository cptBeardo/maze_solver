import random
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
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(None)                
            self._cells.append(column)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j] = Cell(x1, y1, x2, y2, self.win)
        self._cells[i][j].draw()

        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            sleep(0.05) # if I only import time, I would need to do time.sleep()

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        end = self._cells[self.num_cols-1][self.num_rows-1]

        start.has_top_wall = False
        end.has_bottom_wall = False
        
        if self.win:
            start.draw()
            end.draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j-1))
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1, j))
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j+1))
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1, j))

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            
            next_index = random.randrange(len(possible_directions))
            next_i, next_j = possible_directions[next_index]

            current_cell = self._cells[i][j]
            next_cell = self._cells[next_i][next_j]

            if next_i > i:
                current_cell.has_right_wall = False         
                next_cell.has_left_wall = False
            elif next_i < i:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif next_j > j:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif next_j < j:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            
            self._draw_cell(i, j)
            self._draw_cell(next_i, next_j)

            self._break_walls_r(next_i, next_j)

class Cell():
    def __init__(self, x1, y1, x2, y2, win=None):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        

    def draw(self):
        if self._win:
            canvas = self._win.get_canvas()

            """left wall creation"""
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            left_wall = Line(p1, p2)
            if self.has_left_wall:
                left_wall.draw(canvas, fill_color="black")
            else:
                left_wall.draw(canvas, fill_color="#d9d9d9")
            

            """right wall creation"""
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            right_wall = Line(p1, p2)
            if self.has_right_wall:
                right_wall.draw(canvas, fill_color="black")
            else:
                right_wall.draw(canvas, fill_color="#d9d9d9")

            """top wall creation"""    
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            top_wall = Line(p1, p2)
            if self.has_top_wall:
                top_wall.draw(canvas, fill_color="black")
            else:
                top_wall.draw(canvas, fill_color="#d9d9d9")

            """bottom wall creation"""
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            bottom_wall = Line(p1, p2)
            if self.has_bottom_wall:
                bottom_wall.draw(canvas, fill_color="black")
            else:
                bottom_wall.draw(canvas, fill_color="#d9d9d9")

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
