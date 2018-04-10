from matplotlib.dates import DateFormatter
from matplotlib.finance import quotes_historical_yahoo_ohlc
import stock_data
class Stock_list:
    stock_list=[]
    roi=[]
    weekFormatter = DateFormatter('%Y %m %d')
    def __init__(self):
        self.stock_list.clear() 
        self.roi.clear()
    def size(self):
        return len(self.stock_list)
    def read(self,stock_name):
        start = (2011,12,1)
        end = (2016,12,1)
        try:
            quotes=quotes_historical_yahoo_ohlc(stock_name,start,end)
            if len(quotes)==0 :
                raise SystemExit
        except:
            quotes=[]
        for i in range(0,len(quotes)):
            self.insert(quotes[i][0],quotes[i][1],quotes[i][2],quotes[i][3],quotes[i][4],quotes[i][5])
    def insert(self,date,op,high,low,close,vol):
        self.stock_list.append(stock_data.stock_data(date,op,high,low,close,vol))
    def Ma(self,day):
        mat=0
        _ma=[]
        for s in range(0,day-1):
            _ma.append(0)
        for i in range(day-1,len(self.stock_list)):
            for j in range(0,day-1):
                mat+=int(self.stock_list[i-j].getclose())
            _ma.append(float(mat/day))
            mat=0
        return _ma
    def getdate(self,index):
        return self.stock_list[index].getdate()
    def getopen(self,index):
        return self.stock_list[index].getopen()
    def getlow(self,index):
        return self.stock_list[index].getlow()
    def getclose(self,index):
        return self.stock_list[index].getclose()
    def getvol(self,index):
        return self.stock_list[index].getvol()
    def gethigh(self,index):
        return self.stock_list[index].gethigh()
    def getrealtime(self,index):
        return self.weekFormatter(str(int(self.stock_list[index].getdate())))
    def getalldata(self):
        return self.stock_list
    def display(self,index):
        self.stock_list[index].display()
    def tactics(self):
        bi = 0   
        buyin = 0
        allm = 0
        for i in range(0,len(self.stock_list)):
            if self.getopen(i) - self.getclose(i) >= 0 and self.getvol(i) != 0 :
                if (self.getopen(i) - self.getclose(i))/self.getopen(i) <= 0.01 :             
                    if self.getopen(i-1) - self.getclose(i-1) >= 0:
                        buyin = self.getclose(i)
                        bi = i
                        for j in range(0,11):
                            if self.getclose(j) - buyin/buyin < -0.05:
                                bi = j
                        if bi == i:
                            bi += 10
                        if(bi>=len(self.stock_list)):
                            bi=len(self.stock_list)-1
                        self.roi.append(round(100*(self.getclose(bi)-self.getclose(i))/self.getclose(i))/100)
                        allm += self.getclose(bi) - buyin
        return allm
    def getroi(self):
        return self.roi  
    def getroimean(self):
        sum=0
        for i in range(0,len(self.roi)):
            sum += self.roi[i]
        if (sum != 0) and (len(self.roi) != 0) :
            return sum/len(self.roi)
        else:
            return 0
    def getroimax(self):
        flag=0
        for i in range(0,len(self.roi)):
            if self.roi[i]>flag :
                flag=self.roi[i]
        return flag
    def getroimin(self):
        flag=1
        for i in range(0,len(self.roi)):
            if self.roi[i]<flag :
                flag=self.roi[i]
        return flag
    def getroistd(self):
        std=0
        for i in range(0,len(self.roi)):
            std += (self.roi[i]-self.getroimean())**2/len(self.roi)
        std = std**0.5
        return std
    def getroiwinp(self):
        win=0
        for i in range(0,len(self.roi)):
            if self.roi[i] > 0:
                win += 1 
        if len(self.roi) !=0 :
            return win/len(self.roi)
        else:
            return 0
    def getroisum(self):
        sum = 0
        for i in range(0,len(self.roi)):
            sum += self.roi[i]
        return sum
    def getroilen(self):
        return len(self.roi)
        