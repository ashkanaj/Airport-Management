from tkinter import *


class LableEntry:
    def __init__(self, window, text, x, y, distance=60, data_type=StringVar, state="normal"):
        Label(window, text=text).grid(x=x, y=y)
        self.variable = data_type()
        self.entry = Entry(window, textvariable=self.variable, state=state)

        def get(self):
            return self.variable.get()

        def set(self, value):
            self.variable.set(value)


        def reset(self):
            self.variable.set("")

