# pipenv install lxml
# pipenv install twstock
import twstock
# stock = twstock.Stock('2317')
# print(stock.price)



# # 取得某時期資料
# # 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock('2317')  
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019,12)   
for s in stocklist:
    print(s.date.strftime('%Y-%m-%d'), end='\t')
    print(s.open, end='\t')
    print(s.high, end='\t')
    print(s.low, end='\t')
    print(s.close)


import matplotlib.pyplot as plt
import twstock
# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock('2317')  
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019,12)   
listx = []
listy = []
for s in stocklist:
    listx.append(s.date.strftime('%Y-%m-%d'))
    listy.append(s.close)


plt.figure(figsize=[10,5])
plt.title('Foxconn Technology Group 2019-12月 stock',fontsize=18)
plt.xlabel("date",fontsize=14)
plt.ylabel("股價",fontsize=14)
plt.plot(listx, listy, 'r:s')
plt.xticks(rotation=45)
plt.grid('k:', alpha=0.5)
plt.ylim(88,93)
plt.yticks([88,89,90,91,92,93])
plt.rcParams["font.sans-serif"] = "SimHei" 
plt.rcParams["axes.unicode_minus"] = False

plt.show()