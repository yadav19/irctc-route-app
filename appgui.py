from tkinter import *
from header import Header
from body import Body
import trainapi

class Trainapp(Header,Body):

    def __init__(self):
        self.root =Tk()
        self.root.title("IRCTC TRAIN")
        self.root.minsize(800,600)
        self.root.maxsize(800,600)
        self.root.configure(background="#222")
        # # self.l = Label(self.root,text="LABEL ROOT").pack()
        # Trainroute(self.root)
        # # self.f1.pack()
        self.hdr =Header(self.root)
        self.hdr.pack(side=TOP)

        self.bdy = Body(self.root)
        self.bdy.pack(side=TOP)

        self.hdr.send_body(self.bdy)
        # self.button1 = Button(self.root,text="Hello",command = self.ch)
        # self.button1.pack()

    
        # self.x = Trainroute(self.root)
        
    
        





start = Trainapp()
start.root.mainloop()