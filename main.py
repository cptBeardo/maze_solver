from creation import Window, Point, Line


def main():
    win = Window(800, 800)

    """this is for testing"""
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


    win.wait_for_close()


if __name__ == "__main__":
    main()


