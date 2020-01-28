from  tkinter import *
import requests

class irctc:
    def __init__(self):
        
        self.root = Tk()
        self.apikey = "9dgk93tggn"
        self.root.title("IRCTC Train Route")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)

        self.root.configure(background="#00a33a")

        self.label1 = Label(self.root,text="Traing self.root:",bg="#000000",fg="#000fff")
        self.label1.configure(font=("Arial",22,"bold"))
        self.label1.pack(pady=(20,10)) #pady=(upper,lower)

        self.TrainNo = Entry(self.root,text="Train No.:")
        self.TrainNo.pack(ipadx=40,ipady=10)

        self.click = Button(self.root,text="Fetch Stations",bg="#000",fg="#fff",width=15,height=1,command=lambda : self.__fetch())
        self.click.pack(pady=(10,10))

        self.result = Label(self.root,text="",bg="#00a223",fg="#000fff")
        self.result.configure(font=("Contantia",10))
        self.result.pack(pady=(5,10))


        self.root.mainloop()

    def __fetch(self): 
        print(self.TrainNo.get()) # to extract text from an object
        url = "https://api.railwayapi.com/v2/route/train/{}/apikey/{}/".format(self.TrainNo.get(),self.apikey)
        response = requests.get(url)
        data = response.json()

        for i in data["route"]:
            
            self.result = Label(self.root,text="",bg="#000",fg="#fff")
            self.result.configure(font=("Contantia",10),text=i["station"]["name"])
            self.result.pack(pady=(5,10))

rI = irctc()
