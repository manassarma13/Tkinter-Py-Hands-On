from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

#DEFINE

    def createWidgets(self):
        self.CREATE = Button(self)
        self.CREATE["text"] = "Add New Member"
        self.CREATE["fg"]   = "blue"
        self.CREATE["command"] =  self.pack()

        self.CREATE.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

##DISPLAY

    def __init__(self, master=None):
        Frame.__init__(self, master)
#PACK
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
