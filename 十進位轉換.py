from tkinter import*
class test:
    def __init__(self):
        t=Tk()
        t.title('123')
        box = Frame()
        box.pack()
        
        self.v1 = IntVar()
        A=Label(box,text='10進制計算機',bg='yellow',font=('Arial',12))
        A.grid(row = 1 , column = 1)
        B1=Radiobutton(box,text='2',variable = self.v1, value = 2)
        B1.grid(row = 2 , column = 1)
        B2=Radiobutton(box,text='3',variable = self.v1, value = 3)
        B2.grid(row = 2 , column = 2)
        B3=Radiobutton(box,text='4',variable = self.v1, value = 4)
        B3.grid(row = 2 , column = 3)
        B4=Radiobutton(box,text='5',variable = self.v1, value = 5)
        B4.grid(row = 2 , column = 4)
        B5=Radiobutton(box,text='6',variable = self.v1, value = 6)
        B5.grid(row = 2 , column = 5)
        B6=Radiobutton(box,text='7',variable = self.v1, value = 7)
        B6.grid(row = 3 , column = 1)
        B7=Radiobutton(box,text='8',variable = self.v1, value = 8)
        B7.grid(row = 3 , column = 2)
        B8=Radiobutton(box,text='9',variable = self.v1, value = 9)
        B8.grid(row = 3 , column = 3)
        B9=Radiobutton(box,text='10',variable = self.v1, value = 10)
        B9.grid(row = 3 , column = 4)
        B10=Radiobutton(box,text='11',variable = self.v1, value = 11)
        B10.grid(row = 3 , column = 5)
        B11=Radiobutton(box,text='12',variable = self.v1, value = 12)
        B11.grid(row = 4 , column = 1)
        B12=Radiobutton(box,text='13',variable = self.v1, value = 13)
        B12.grid(row = 4 , column = 2)
        B13=Radiobutton(box,text='14',variable = self.v1, value = 14)
        B13.grid(row = 4 , column = 3)
        B14=Radiobutton(box,text='15',variable = self.v1, value = 15)
        B14.grid(row = 4 , column = 4)
        B15=Radiobutton(box,text='16',variable = self.v1, value = 16)
        B15.grid(row = 4 , column = 5)
        
        box1=Frame()
        box1.pack()
        
        self.v2=StringVar()
        C=Label(box1,text='10進位數字為:')
        C.grid(row=1,column=1)
        D = Entry(box1,textvariable = self.v2,font=('Arial', 15))
        D.grid(row=1,column=2)
        
        E = Button(box1, text="換算", command=self.hit_me)
        E.grid(row=1,column=3)
        
        
        self.F=Label(box1,text='')
        self.F.grid(row=2,column=1)
        self.G=Label(box1,text='')
        self.G.grid(row=2,column=2)
        
        
        
        
        t.mainloop()
    def hit_me(self):
        n=int(self.v2.get())
        x=int(self.v1.get())
        a=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
        b=[]
        while True:
            s=n//x
            y=n%x
            b=b+[y]
            if y<=9:
                y=(chr(y+55))
            if s<1:
                break
            n=s
        b.reverse()
        if self.v1.get()==2:
            self.F["text"] = "2進制為:"
        elif  self.v1.get()==3:
            self.F["text"] = "3進制為:"
        elif  self.v1.get()==4:
            self.F["text"] = "4進制為:"
        elif  self.v1.get()==5:
            self.F["text"] = "5進制為:"
        elif  self.v1.get()==6:
            self.F["text"] = "6進制為:"
        elif  self.v1.get()==7:
            self.F["text"] = "7進制為:"
        elif  self.v1.get()==8:
            self.F["text"] = "8進制為:"
        elif  self.v1.get()==9:
            self.F["text"] = "9進制為:"
        elif  self.v1.get()==10:
            self.F["text"] = "10進制為:"
        elif  self.v1.get()==11:
            self.F["text"] = "11進制為:"
        elif  self.v1.get()==12:
            self.F["text"] = "12進制為:"
        elif  self.v1.get()==13:
            self.F["text"] = "13進制為:"
        elif  self.v1.get()==14:
            self.F["text"] = "14進制為:"
        elif  self.v1.get()==15:
            self.F["text"] = "15進制為:"
        else:
            self.v1.get()==16
            self.F["text"] = "16進制為:"
        self.G["text"] = b
        
        
def main():  
    test()
if __name__=='__main__':
        main()
        