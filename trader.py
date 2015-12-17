from yahoo_finance import Share
from pprint import pprint
import urllib2
import requests
import re

"""
    This method gets the current price from the ticker
    if the ticker is accurate then the string value is returned
    if the ticker is not valid then None is returned
"""
def getCurrentPriceFromTicker(ticker):
    stocks = Share(ticker.replace("." , "-"))
    return stocks.get_price()


"""
    This returns the edited array of results from the ticker
    if it is valid. if the ticker is invalid then None returned
    form of the array
    sorted(student_tuples, key=lambda student: student[2])
"""
def getHistoricalPriceFromRange(ticker, start, end):
    stocks = Share(ticker.replace("." , "-"))
    answerList = []
    for item in (stocks.get_historical(start,end)):
        answerList.append( (item['Date'],item["Low"] , item["High"] , item["Close"],item["Open"]) )
    pprint (answerList)



"""
    This method takes the companyName and displays a list of companies
    their stock symbol and their trading market and returns a dictionary of the following formatString
    [stockSymbol] = (price , name of company, trading market)
"""
def searchForCompany(companyName):
    stockDictionary = {}
    prefix = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/jsonp?input='
    suffix = '&callback=myFunction'
    url = prefix + companyName + suffix

    response = requests.get(url)
    resultList = removeBracesDictFromResults(response.content)

    if resultList:
        for item in resultList[:len(resultList) - 1]:

            stocklist = removeDictWithColon(item)
            ticker = stocklist[0].split(":")[1]
            stockDictionary[ticker] = (getCurrentPriceFromTicker(ticker) , stocklist[1].split(":")[1] , stocklist[2].split(":")[1])

        for items in stockDictionary:
            print items , stockDictionary[items]
        return stockDictionary
    else:
        return None


"""
    This list removes {} from a dictionary. it removes the individual
    pieces from the string and returns it in the form of list.
"""
def removeBracesDictFromResults(string):
    answer = re.search('{(.*)}', string)
    if answer:
        result = answer.group()
        if result:
            resultList = result.split('}')
            resultList[0] = resultList[0].replace("{" , "")
            return resultList
    else:
        return None


""""
    Given a list with colon sepeared items This method takes care of the extra {}() at the
    ends and then returns a list of key values seperated by :
"""
def removeDictWithColon(item):
        itemWithoutQuotes = item.replace("\"" , "")
        formatString = itemWithoutQuotes.replace(",{" , "")
        stocklist = formatString.split(",")
        return stocklist



while(True):
    selector = raw_input('1: for stocks\n2: for company lookup\n3: for historical lookup\nquit: for quit ')
    if selector == '1':
        ticker = raw_input('enter ticker: ')
        if getCurrentPriceFromTicker(ticker):
            print getCurrentPriceFromTicker(ticker)
        else:
            print 'wront ticker try again'
            continue
    elif selector == '2':
        ticker = raw_input('companyName: ')
        if searchForCompany(ticker):
            searchForCompany(ticker)
        else:
            print 'no company found'
            continue
    elif selector == '3':
        ticker = raw_input('stok name: ')
        start = raw_input('start: ')
        end = raw_input('end: ')
        getHistoricalPriceFromRange(ticker, start, end)
    elif selector == 'quit':
        break
