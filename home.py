from  tkinter import *

class irctc:
    def __init__(self):
        self.root = Tk()
        self.root.title("IRCTC Train Route")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)

        self.root.configure(background="#00a33a")

        self.label1 = Label(self.root,text="Traing self.root:",bg="#000",fg="#fff")
        self.label1.configure(font=("Arial",22,"bold"))
        self.label1.pack(pady=(20,10)) #pady=(upper,lower)

        self.TrainNo = Entry(self.root,text="Train No.:")
        self.TrainNo.pack(pady=(10,10))

        self.click = Button(self.root,text="Fetch Stations",bg="#123",fg="#345",width=15,height=1,font=("Arial",10))
        self.click.pack(pady=(10,10))

        self.result = Label(self.root,text="",bg="")
        self.result.configure(font=("Contantia",10))
        self.result.pack(pady=(5,10))


        self.root.mainloop()