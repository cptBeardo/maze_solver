from tkinter import Tk, BOTH, Canvas

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