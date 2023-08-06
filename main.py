from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(20, 20)), "red")
    win.draw_line(Line(Point(0, 0), Point(500, 20)), "black")
    win.wait_for_close()

if __name__ == '__main__':
    main()