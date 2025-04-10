from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        #self.width = width  # not included in solution file?
        #self.height = height  # not included in solution file?
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close) # add after creating redraw(), wait_to_close(), and close() methods
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width) # can have any number of parameters, but must have the master (this case, self.__root)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update() 

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...", flush=True) # not in my original code, but was in the solution file, so I added it because I like it

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    #def get_canvas(self):
    #    return self.__canvas
 
    def close(self):
        self.__running = False

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
