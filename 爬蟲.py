import requests
import csv
year='2019'
mon1='1'
mon2='12'
stockNo='2330'

csvfile="stock2330.csv"

 
with open (csvfile, 'w+',newline='') as fp:
    writer=csv.writer(fp)
    mon=int(mon1)
    while mon<=int(mon2):
        if mon<10:
            datestr=year + '0' + str(mon)+'01'
        else:
            datester=year + str(mon) +'01'
        url='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='
        r=requests.post(url + datestr + '&stockNo=' +stockNo)
        data=r.json()
        for item in data['data']:
            writer.writerow(item[0:])
        mon += 1