from yahoo_finance import Share
from pprint import pprint

stocks = Share('GOijG')
pprint( stocks.get_historical('2015-12-01' ,'2015-12-15' ) )
print '------------------FETCHING PRICE==----------------------------------'
print stocks.get_price();
