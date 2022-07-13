import csv
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

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
    
    plt.show()