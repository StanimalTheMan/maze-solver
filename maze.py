import time
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for row in range(self._num_rows):
            # list of cell objects
            self._cells = [Cell(self._win) for _ in range(self._num_cols)]

        #  draw each Cell
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._draw_cell(row, col)
                
    def _draw_cell(self, i, j):
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = self._x1 + (j + 1) * self._cell_size_x
        y2 = self._y1 + (i + 1) * self._cell_size_y
        self._cells[i].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)