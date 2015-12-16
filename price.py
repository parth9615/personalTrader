from yahoo_finance import Share
from pprint import pprint

stocks = Share('GOOG')
pprint( stocks.get_historical('2015-12-01' ,'2015-12-15' ) )
