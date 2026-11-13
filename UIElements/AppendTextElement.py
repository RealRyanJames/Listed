from tkinter import *


class AppendUIElements:
    def __init__(self, TextEl, root):

        self.text = TextEl
        self.label = Label(root, text=self.text)

    def ShowLabel(self) -> bool:
        if self.label is not None:
            return True
