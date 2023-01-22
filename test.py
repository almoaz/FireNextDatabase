from tkinter import *

root = Tk()

root.geometry("300x300")


def onPosition(event):
    print("Position")


btn = Button(root, text="button")
btn.pack()

btn.bind("<Enter>", onPosition)

root.mainloop()
