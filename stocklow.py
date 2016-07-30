from yahoo_finance import Share
import operator
from collections import Counter
from collections import Counter
from pprint import pprint

stocks = [("AMZN",1997) , ("AAPL",1980) , ("GOOG",2004) , ("FB",2012) , ("NFLX",2002) , ("F",1978) , ("MSFT",1986) ]
overallLow = []
overallHigh = []
ans = []
for i in stocks:
    name = i[0]
    stock = Share(i[0])
    year = i[1]
    print '------------------------' , i[0] , '--------------------------'

    lowMonth = []
    highMonth = []
    relation = []
    for j in range(2016 - i[1]):
        year += 1
        a = stock.get_historical( str(year)+'-01-01', str(year)+'-12-31')

        low = {}
        high = {}

        for i in a:
            low[i['Date']] = i['Low']

            high[i['Date']] = i['High']

        sortedLow = sorted(low.items(), key=operator.itemgetter(1))
        sortedHigh = sorted(high.items(), reverse=True, key=operator.itemgetter(1))

        lowMonth.append(sortedLow[0][0][5:7])
        overallLow.append(sortedLow[0][0][5:7])

        highMonth.append(sortedHigh[0][0][5:7])
        overallHigh.append(sortedHigh[0][0][5:7])
        print 'low:: ' , sortedLow[0] , '::high:: ' , sortedHigh[0]
        co = str(sortedLow[0][0][5:7]) , str(" : ") , str(sortedHigh[0][0][5:7])
        relation.append(co)
        ans.append(co)




    count = Counter(lowMonth)
    print 'low::::::::::::::::::::', name, count.most_common()
    count = Counter(highMonth)
    print 'high:::::::::::::::::::', name, count.most_common()
    count = Counter(relation)
    print 'realations:::::::::::::' , name , count.most_common()

count = Counter(overallLow)
print 'low::::::::::::::::::::',count.most_common()
count = Counter(overallHigh)
print 'high:::::::::::::::::::',count.most_common()
count = Counter(ans)
print 'realations:::::::::::::' , name , count.most_common()
