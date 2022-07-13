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
    
    x=[datetime.strptime(d,'%m/%d').date() for d in myDay]
    Volumn=[]
    for v in myVol:
        Volumn.append(int(v.replace(',','')))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=45))
    plt.plot(x,myPrice)
    
    MAarray=[]
    MA=[]
    MAValue= 0
    MAlen=20
    
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
    
    plt.plot(x[MAlen:],MA[MAlen:],'r-')
    plt.show()

    