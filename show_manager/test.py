from tkinter import *

root = Tk()

premadeList = ["foo", "bar", "baz"]

for checkBoxName in premadeList:
    c = Checkbutton(root, text=checkBoxName)
    c.pack()

root.mainloop()