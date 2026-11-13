from UIElements.UIElements import Win
from UIElements.UIElements import SizesUISizer
from UIElements.AppendTextElement import AppendUIElements
from tkinter import *
import os
import sys

root = Tk()
win = Win(True)

class Log:
    def __init__(self):
        self.isAppended = True

    def isLog(self) -> bool:
        return self.isAppended

def logFile() -> bool:
    log = Log()
    return log.isLog()

def appendFile(text_1: str, text_2: str) -> None:

    if logFile():

        with open("todos.txt", "a") as f:
            f.write(text_1 + "\n")
            f.write(text_2 + "\n")

if win.isEnabled():

    app =  AppendUIElements("Enter Todo 1: ", root)
    app1 = AppendUIElements("Enter Todo 2: ", root)

    if app.ShowLabel():

        size = SizesUISizer(250, 250)
        text = Text(root, height = -20, width=90 - 50, font=("sans-serif", 14))

        app.label.pack()
        text.pack()
        root.geometry(size.Geo())

        text1 = Text(root, height=-20, width=40, font=("sans-serif", 14))

        def get_text():
            text_value = text.get("1.0", "end-1c")
            print("Text: ", text_value)
            text_1 = text1.get("1.0", "end-1c")
            print("Text: ", text_1)

            appendFile(text_1=text_value, text_2=text_1)

        b = Button(text="Submit", command=get_text)

        app1.label.pack()
        text1.pack()
        b.pack()
        root.mainloop()


sys.exit(os.EX_OK)