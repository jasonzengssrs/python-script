#多进程抓取每天的股票行情
import tushare as ts
import multiprocessing
import pandas as pd

class Stock:
    def __init__(self):
        self.stockcode = sorted(list(ts.get_stock_basics().index))

        mgr = multiprocessing.Manager()
        self.wrong = mgr.list()
    

    def get_stock(self,code,start='2017-07-10',end='2017-07-10'):
        try:
            print("getting %s"%code)
            return ts.get_k_data(code,start,end)

        except:
            print("抓取%s出错"%code)
            self.wrong.append(code)

    
    def run(self,n=0,m=10):
        df = pd.DataFrame()

        
        pool = multiprocessing.Pool(processes=4)
        result = pool.map(self.get_stock,self.stockcode[0:10])
        
        result = list(result)

        for i in range(len(result)):
            df1  = pd.DataFrame(result[i])
            df = df.append(df1)

        print('抓取%s出错'%self.wrong)
        print(df)




if __name__ == '__main__':
    stock = Stock()
    stock.run()
   

   