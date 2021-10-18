from Tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Help a friend")
myLabel2 = Label(root, text = "Don't help a friend")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
