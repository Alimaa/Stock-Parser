import time
import datetime
import array
import pandas as pd
import urllib2
import smtplib

#This program parse the stock price between specific hours and generate
#a data frame


def parsePrice():
    
    url = "http://www.google.com/finance?cid="+str(38688)
    contents = urllib2.urlopen(url).read()
    string = 'values:["WDC","Western Digital Corp","'
    
    l = contents.find(string)
    x = l + len(string)
    
    val = float(contents[x:x+6])
    return(val)

def priceHist(startHr,startMin,endHr,endMin,secInt):

    t=[]
    p=[]
    
    while ((time.localtime()[3:5]<=(endHr,endMin))&(time.localtime()[3:5]>=(startHr,startMin))):
        
        if ((time.localtime()[5]%secInt)==0):
            
            t.append(time.localtime())
            p.append(parsePrice())
            time.sleep(2)
    
    data = {'time':t , 'price': p}
    df = pd.DataFrame(data)
    
    return(df)
  

while time.localtime()[3:5]<(17,00):

    df = priceHist(6,30,13,00,5)

    if df.empty==False:
        print cnt
        break

        
                