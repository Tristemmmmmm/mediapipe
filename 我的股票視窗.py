import csv
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np 
class From:
    def __init__(self):
        self.root=tk.Tk()
        self.canvas=tk.Canvas()
        self.topbutton()
        self.figure=self.create_matplotlib()
        self.create_form(self.figure)
        self.root.mainloop()
    def topbutton(self):
        box1 = tk.Frame(self.root)
        box1.pack()
        ma5=tk.Button(box1,text='MAlen5',bg='white',command=self.MAlen5)
        ma5.grid(row =  0, column = 0)
        ma20=tk.Button(box1,text='MAlen20',bg='white',command=self.MAlen20)
        ma20.grid(row = 0 , column = 1)
        ma60=tk.Button(box1,text='MAlen60',bg='white',command=self.MAlen60)
        ma60.grid(row = 0 , column = 2)
    def MAlen5(self):
        plt.clf
        f=plt.figure(figsize=(5,4), dpi=100)
        fig=plt.subplot(1,1,1)
        csvfile="stock2330.csv"
        with open(csvfile,'r') as fp:
            reader=csv.reader(fp)
            myDay=[]
            myPrice=[]
            myVol=[]
            
            for newline in reader:
                myDay.append(newline[0][4:])
                myPrice.append(float(newline[6]))
                myVol+=[newline[1]]
            x=[datetime.strptime(d,'%m/%d').date() for d in myDay]
            Volumn=[]
            
            for v in myVol:
                Volumn.append(int(v.replace(',','')))  
            MAarray=[]
            MA=[]
            MAValue= 0
            MAlen=5#均線
            
            for i in myPrice:
                if len(MAarray)==0:
                    MAarray+=[i]
                else:
                    if len(MAarray)==MAlen:
                        MAarray=MAarray[1:]+[i]
                    else:
                        MAarray+=[i]
                MAValue=float(sum(MAarray))/len(MAarray)
                MA.append(MAValue)
            
            fig=plt.figure(1)
            ax1=fig.add_subplot(211)
            
            ax1.plot(x,myPrice,'k-')
            ax1.plot(x[MAlen:],MA[MAlen:],'r-')
            
            ax2=fig.add_subplot(212)
            ax2.bar(x,Volumn)
            
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax1.xaxis.set_major_locator(mdates.DayLocator(interval=45))
            
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax2.xaxis.set_major_locator(mdates.DayLocator(interval=45))
            
           
        
        return f
    def MAlen20(self):
        plt.clf()
        f=plt.figure(figsize=(5,4), dpi=100)
        fig=plt.subplot(1,1,1)
        csvfile="stock2330.csv"
        with open(csvfile,'r') as fp:
            reader=csv.reader(fp)
            myDay=[]
            myPrice=[]
            myVol=[]
            
            for newline in reader:
                myDay.append(newline[0][4:])
                myPrice.append(float(newline[6]))
                myVol+=[newline[1]]
            x=[datetime.strptime(d,'%m/%d').date() for d in myDay]
            Volumn=[]
            
            for v in myVol:
                Volumn.append(int(v.replace(',','')))  
            MAarray=[]
            MA=[]
            MAValue= 0
            MAlen=20#均線
            
            for i in myPrice:
                if len(MAarray)==0:
                    MAarray+=[i]
                else:
                    if len(MAarray)==MAlen:
                        MAarray=MAarray[1:]+[i]
                    else:
                        MAarray+=[i]
                MAValue=float(sum(MAarray))/len(MAarray)
                MA.append(MAValue)
            
            fig=plt.figure(1)
            ax1=fig.add_subplot(211)
            
            ax1.plot(x,myPrice,'k-')
            ax1.plot(x[MAlen:],MA[MAlen:],'r-')
            
            ax2=fig.add_subplot(212)
            ax2.bar(x,Volumn)
            
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax1.xaxis.set_major_locator(mdates.DayLocator(interval=45))
            
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax2.xaxis.set_major_locator(mdates.DayLocator(interval=45))
            
           
        
        return f
    def MAlen60(self):
        plt.clf()
        f=plt.figure(figsize=(5,4), dpi=100)
        fig=plt.subplot(1,1,1)
        csvfile="stock2330.csv"
        with open(csvfile,'r') as fp:
            reader=csv.reader(fp)
            myDay=[]
            myPrice=[]
            myVol=[]
            
            for newline in reader:
                myDay.append(newline[0][4:])
                myPrice.append(float(newline[6]))
                myVol+=[newline[1]]
            x=[datetime.strptime(d,'%m/%d').date() for d in myDay]
            Volumn=[]
            
            for v in myVol:
                Volumn.append(int(v.replace(',','')))  
            MAarray=[]
            MA=[]
            MAValue= 0
            MAlen=60#均線
            
            for i in myPrice:
                if len(MAarray)==0:
                    MAarray+=[i]
                else:
                    if len(MAarray)==MAlen:
                        MAarray=MAarray[1:]+[i]
                    else:
                        MAarray+=[i]
                MAValue=float(sum(MAarray))/len(MAarray)
                MA.append(MAValue)
            
            fig=plt.figure(1)
            ax1=fig.add_subplot(211)
            
            ax1.plot(x,myPrice,'k-')
            ax1.plot(x[MAlen:],MA[MAlen:],'r-')
            
            ax2=fig.add_subplot(212)
            ax2.bar(x,Volumn)
            
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax1.xaxis.set_major_locator(mdates.DayLocator(interval=45))
            
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax2.xaxis.set_major_locator(mdates.DayLocator(interval=45))
            
           
        
        return f
    def create_matplotlib(self):
        f=plt.figure(figsize=(5,4), dpi=100)
        fig=plt.subplot(1,1,1)
        csvfile="stock2330.csv"
        with open(csvfile,'r') as fp:
            reader=csv.reader(fp)
            myDay=[]
            myPrice=[]
            myVol=[]
            
            for newline in reader:
                myDay.append(newline[0][4:])
                myPrice.append(float(newline[6]))
                myVol+=[newline[1]]
            x=[datetime.strptime(d,'%m/%d').date() for d in myDay]
            Volumn=[]
            
            for v in myVol:
                Volumn.append(int(v.replace(',','')))  
            MAarray=[]
            MA=[]
            MAValue= 0
            MAlen=20#均線
            
            for i in myPrice:
                if len(MAarray)==0:
                    MAarray+=[i]
                else:
                    if len(MAarray)==MAlen:
                        MAarray=MAarray[1:]+[i]
                    else:
                        MAarray+=[i]
                MAValue=float(sum(MAarray))/len(MAarray)
                MA.append(MAValue)
            
            fig=plt.figure(1)
            ax1=fig.add_subplot(211)
            
            ax1.plot(x,myPrice,'k-')
            ax1.plot(x[MAlen:],MA[MAlen:],'r-')
            
            ax2=fig.add_subplot(212)
            ax2.bar(x,Volumn)
            
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax1.xaxis.set_major_locator(mdates.DayLocator(interval=45))
            
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax2.xaxis.set_major_locator(mdates.DayLocator(interval=45))
            
           
        
        return f
    def create_form(self,figure):
        self.canvas=FigureCanvasTkAgg(figure,self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        
        toolbar=NavigationToolbar2Tk(self.canvas,self.root)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        
if __name__=="__main__":
    From()