from tkinter import *


class OperationButton:
    def __init__(self, window, labels=["save", "add", "remove"], functions=[], x=[20, 90, 110],
                 y=[300, 300, 300]):
        Button(window, text=labels[0], width=6, command=functions[0]).place(x=x[0], y=y[0])
        Button(window, text=labels[1], width=6, command=functions[1]).place(x=x[1], y=y[1])
        Button(window, text=labels[2], width=6, command=functions[2]).place(x=x[2], y=y[2])
