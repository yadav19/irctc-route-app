from tkinter import *
from trainapi import *
class Body(Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self["height"] = 550
        self["width"] = 800
        self["bg"] = "#222"
        self.initialroute = Trainroute(self)
        # self.initialroute.input_frame.pack(side=TOP)


class Trainroute(Train):
    def __init__(self,p):
        self.input_frame = Frame(p,height=50,width=800,bg="#222")
        self.input_train_label = Label(self.input_frame,text="Search Train:",font=("Arial",10,"bold"),bg="#222",fg="#ccc").pack(side=LEFT,pady=5) 
        self.input_train_no = Entry(self.input_frame,width=30)
        # self.input_train_button = Button(self.input_frame,font=("Arial",10,"bold"),width=25,height=1,bg="#ccc",text="Search",fg = "#fff").pack(side=LEFT)
        self.input_train_no.bind("<Return>",self.game)
        self.input_train_no.pack(side=LEFT,pady=5,padx=20,ipadx=5,ipady=3)
        self.input_frame.pack(side=TOP)

        self.output_frame = Frame(p,height=500,width=800,bg="#333")
        self.output_text = Text(p,height=495,width=795,bg="#fff").pack()
        self.output_frame.pack(side=TOP)

    def game(self):
        print("APXX")

class Trainlive(Train):
    def __init__(self):
        pass

class Stationlive(Train):
    def __init__(self):
        pass
