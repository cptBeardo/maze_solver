from cell import Cell
import random
from time import sleep

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):        
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))                
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            sleep(0.05) # if I only import time, I would need to do time.sleep()

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        end = self._cells[self._num_cols-1][self._num_rows-1]

        start.has_top_wall = False
        self._draw_cell(0, 0)
        end.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        
        # DEBUGGING if self._win:
        # DEBUGGING     start.draw()
        # DEBUGGING     end.draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j-1))
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1, j))
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
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

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _solve_r(self, i, j):
        # print(f"Visiting cell {i},{j}", flush=True)
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            print("Found the exit!", flush=True)
            return True

        # move left if there is no wall and it hasn't been visited
        if (i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't  been visited
        if (i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False

    def solve(self):
        print("Starting maze solving", flush=True)
        result = self._solve_r(0, 0)
        print(f"Maze solving complete: {result}", flush=True)
        return result

