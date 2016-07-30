import csv
import sys
from collections import OrderedDict
from operator import itemgetter
from collections import Counter

def getYear():
    return i[0].split("/")[-1]

def getMonth():
    return int(i[0].split("/")[0])

def getDay():
    return int(i[0].split("/")[1])

month = {
            1 : 'Jan',
            2 : 'Feb',
            3 : 'March',
            4 : 'April',
            5 : 'May',
            6 : 'June',
            7 : 'July',
            8 : 'Aug',
            9 : 'Sep',
            10: 'Oct',
            11 : 'Nov',
            12 : 'Dec'
    }
stocks = [("amzn" , "amzn.csv") , ("goog","goog.csv") , ("apple" , "aapl.csv")]
for i in stocks:
    nameOfStocks = i[0]
    nameOfFile = i[1]
    file = open(nameOfFile)
    fileReader = csv.reader(file)
    listOfData = list(fileReader)
    print '-----------------------------------' , nameOfStocks , '---------------------------------------------------'

    year = '16'
    low = 1000000000000000000000.0;
    high = -1.0;
    lowMonth = ""
    highMonth = ""
    counter = 0
    overallLow = []
    overallHigh = []
    year = listOfData[1][0].split("/")[-1]
    lowDay = ""
    highDay = ""
    trends = []
    lowAndHigh = []
    for i in listOfData[1:]:

        if getYear()  == year:
            currLow = float(i[2])
            currHigh = float(i[3])


            if currLow < low:
                low = currLow
                lowMonth = getMonth()
                lowDay = getDay()
            if currHigh > high:
                high = currHigh
                highDay = getDay()
                highMonth = getMonth()
        else:
           
            print getYear() , '[ Low: ' , month[lowMonth] , lowDay, " ]: " ,  '  [high: ' , month[highMonth], highDay , " ] : [" , low , high , ']'
            lowToHigh = str(month[lowMonth]) , ":" , str(month[highMonth])
            lowAndHigh.append((low , high))
            trends.append(lowToHigh)
            overallLow.append(month[lowMonth])
            overallHigh.append(month[highMonth])
            year = getYear()
            low = 1000000000000000000000.0;
            high = -1.0;

    ans = Counter(overallLow)
    print 'Low: ' , ans.most_common(4)
    ans = Counter(overallHigh)
    print 'High: ' , ans.most_common(4)
    c = Counter(trends)
    print c.most_common(3)



            



