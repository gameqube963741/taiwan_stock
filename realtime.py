# import twstock
# # 以鴻海的股票代號建立 Stock 物件
# stock = twstock.Stock('2317')  
# # 取得 2019 年 12 月的資料
# stocklist = stock.fetch(2019,12)   
# for s in stocklist:
#     print(s.date.strftime('%Y-%m-%d'), end='\t')
#     print(s.open, end='\t')
#     print(s.high, end='\t')
#     print(s.low, end='\t')
#     print(s.close)
import twstock
real = twstock.realtime.get('2317')
{'timestamp':1578033000.0,
'info':{
    'code':'2317',
    'channeal':'2317.tw',
    'name':'鴻海',
    'fullname':'鴻海精密工業股份有限公司',
    'time':'2020-01-03 14:30:00',
    'realtime':{
        'latest_trade_price':'91.60',
        'trade_volume':'2406',
        'accumulate_trade_volume':'37546',
        'best_bid_price':['91.50','91.40','91.30','91.20'],
        'best_bid_volume':['38','2','64','293','227'],
        'best_ask_price':['91.60','91.70','91.80','91.90'],
        'best_ask_volume':['258','799','820','1133','2874'],
        'open':'91.40',
        'high':'92.20',
        'low':'90.80'},
'success':True}}

print(real['realtime']['latest_trade_price'])

# 鴻海股票即時交易資訊
real = twstock.realtime.get('2317') 
if real['success']:  #如果讀取成功
    print('即時股票資料：',real['info']['name'])     
    print('開盤價：',real['realtime']['open'], end=', ')
    print('最高價：',real['realtime']['high'], end=', ')  
    print('最低價：',real['realtime']['low'], end=', ')
    print('目前股價：',real['realtime']['latest_trade_price'])   
else:
    print('錯誤：' + real['rtmessage'])  

