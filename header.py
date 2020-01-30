from tkinter import *
class Header(Frame):
    def changecolor1(self):
        pass
    def changecolor2(self):
        pass
    def changecolor3(self):
        pass
    def changecolor4(self):
        pass
    def __init__(self,parent):
        super().__init__(parent)
        self["height"] = 50
        self["width"] = 800
        # self["releif"] = FLAT
        self["bg"] = "#224"
        self.c1 = "#333"
        self.c2 = "#666"
        self.c3 = "#666"
        self.c4 = "#666"
        
        self.route_button = Button(self,text = "TRAIN ROUTE",font=("Arial",10,"bold"),width=25,height=1,bg="{}".format(self.c1),bd=0,fg="#fff",command= self.changecolor1).pack(side=LEFT,ipady=3,padx=2)        
        self.live_train_button = Button(self,text = "LIVE TRAIN STATUS",font=("Arial",10,"bold"),width=25,height=1,bg="{}".format(self.c2),bd=0,fg="#fff",command= self.changecolor2).pack(side=LEFT,ipady=3,padx=2)
        self.sation_button = Button(self,text = "LIVE STATION STATUS",width=25,height=1,bg="{}".format(self.c3),font=("Arial",10,"bold"),bd=0,fg="#fff",command= self.changecolor3).pack(side=LEFT,ipady=3,padx=2)
        self.apikey_setting_button = Button(self,text = "SETTINGS",width=25,height=1,bg="{}".format(self.c4),font=("Arial",10,"bold"),bd=0,fg="#fff",command= self.changecolor4).pack(side=LEFT,ipady=3,padx=2)
    
    def send_body(self,body):
        self.parentbody = body