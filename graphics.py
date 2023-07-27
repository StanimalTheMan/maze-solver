from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Python Maze Solver App")
        self._canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._is_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()

    def close(self):
        self._is_running = False