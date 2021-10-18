from Tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Clicked!")
    myLabel.pack()

myButton = Button(root,text="Click Me",command=myClick, fg= 'blue', bg='red')
myButton.pack()

root.mainloop()
