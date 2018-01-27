from tkinter import *
from random import *


class RedDotsCanvas(object):

    def __init__(self, width: int, height: int, refresh_rate: int = 100):

        self.real_size = (width, height)
        self.refresh_rate = refresh_rate

        self.window = Tk()
        self.window.title("Окошко")

        self.canvas = Canvas(self.window, width=self.real_size[0], height=self.real_size[1])

        self.run()
        self.window.mainloop()

    def run(self):

        self.canvas.delete("all")

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill = "Red", outline = "" )
        if self.x > self.w or self.x < 0:
            self.dx = - self.dx
        if self.y > self.h or self.y < 0:
            self.dy = - self.dy

        self.window.after(self.refresh_rate, self.run)


RedDotsCanvas(800, 800, 1)