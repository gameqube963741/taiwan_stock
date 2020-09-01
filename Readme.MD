<!-- 即時股市爬取 -->
# twstock台灣股市專用模組抓取即時股價，並實現視覺化

pip install twstock
import twstock
stock = tw.stock.Stock('2317')

# 屬性：
date / 日期
capacity / 交易股數(單位：股)
turnover / 交易金額(單位：元)
open / 開盤價
high / 最高價
low / 最低價
price / 收盤價
close / 收盤價
change / 漲跌差價
transaction / 交易筆數