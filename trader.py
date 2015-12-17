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
"""
def getHistoricalPriceFromRange(ticker, start, end):
    stocks = Share(ticker.replace("." , "-"))
    return stocks.get_historical(start,end)


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
    result = re.search('{(.*)}', response.content)

    if result:
        resultList = result.group().split('}')
        resultList[0] = resultList[0].replace("{" , "")

        for item in resultList[:len(resultList) - 1]:
            itemWithoutQuotes = item.replace("\"" , "")
            formatString = itemWithoutQuotes.replace(",{" , "")

            stocklist = formatString.split(",")
            ticker = stocklist[0].split(":")[1]
            stockDictionary[ticker] = (getCurrentPriceFromTicker(ticker) , stocklist[1].split(":")[1] , stocklist[2].split(":")[1])


        for items in stockDictionary:
            print items , stockDictionary[items]
    return stockDictionary
    else:
        return None


print '1: getPrice \n2:searchForCompany'
selector = raw_input('enter 1 or 2: ')
if selector == '1':
    ticker = raw_input('enter ticker: ')
    print getCurrentPriceFromTicker(ticker)
elif selector == '2':
    ticker = raw_input('companyName: ')
    searchForCompany(ticker)
