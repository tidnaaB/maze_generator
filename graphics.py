# Imports
from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    # redraw() method
    def redraw(self):
        # Call The root Widgets update_idletasks() and update() methods
        self.__root.update_idletasks()
        self.__root.update()

    # wait_for_close() method
    def wait_for_close(self):
        # Set the running data membe to True
        self.__running = True
        # While the running data member is True, call the redraw() method
        while self.__running:
            self.redraw()
        print("Window closed, game over.")

    # draw_line() method
    def draw_line(self, line, fill_color="black"):
        # Call the draw() method on the line object
        line.draw(self.__canvas, fill_color)

    # close() method
    def close(self):
        # Set the running data member to False
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
