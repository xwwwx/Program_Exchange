class stock_data:
       def __init__(self,date,op,high,low,close,vol): 
           self.date=date
           self.open=op
           self.close=close
           self.high=high
           self.low=low
           self.vol=vol
       def getdate(self):
           return self.date
       def getopen(self):
           return self.open
       def getlow(self):
           return self.low
       def getclose(self):
           return self.close
       def getvol(self):
           return self.vol
       def gethigh(self):
           return self.high
       def display(self):
           print("date:",self.date)
           print("open:",self.open)
           print("high:",self.high)
           print("low:",self.low)
           print("close:",self.close)
           print("vol:",self.vol)