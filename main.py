from creation import Window, Point, Line, Cell, Maze


def main():
    win = Window(800, 800)

    """this is for testing lines"""
    p1 = Point(100, 100)
    p2 = Point(700, 100)
    p3 = Point(100, 500)
    p4 = Point(700, 500)

    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p1, p3)
    line4 = Line(p2, p4)
    line5 = Line(p1, p4)

    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")
    win.draw_line(line4, "purple")
    win.draw_line(line5, "orange")
    """end of the test lines"""

    """start tests for Cell() creation"""
    cell1 = Cell(50, 50, 100, 100, win)
    cell1.draw()

    cell2 = Cell(150, 50, 200, 100, win)
    cell2.has_right_wall = False
    cell2.draw()

    cell3 = Cell(50, 150, 100, 200, win)
    cell3.has_bottom_wall = False
    cell3.draw()

    cell4 = Cell(150, 150, 200, 200, win)
    cell4.has_left_wall = False
    cell4.has_top_wall = False
    cell4.draw()
    """end tests for Cell() creation"""

    """start tests for solution line"""
    cell1.draw_move(cell2)
    cell2.draw_move(cell1, undo=True)
    cell2.draw_move(cell4)
    """end tests for solution line"""


    win.wait_for_close()


if __name__ == "__main__":
    main()


