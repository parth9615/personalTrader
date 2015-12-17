from yahoo_finance import Share
from pprint import pprint
import urllib2
import requests

"""
    This method gets the current price from the ticker
    if the ticker is accurate then the string value is returned
    if the ticker is not valid then None is returned
"""
def getCurrentPriceFromTicker(ticker):
    stocks = Share(ticker)
    return stocks.get_price()


"""
    This returns the edited array of results from the ticker
    if it is valid. if the ticker is invalid then None returned
"""
def getHistoricalPriceFromRange(ticker, start, end):
    stocks = Share(ticker)
    return stocks.get_historical(start,end)


"""
    This method takes the companyName and fetches an array of
    company resembling the input and displays it for the user to pick
"""
def searchForCompany(companyName):
    prefix = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/jsonp?input='
    suffix = '&callback=myFunction'
    url = prefix + companyName + suffix

    response = requests.get(url)
    return response.content




print '1: getPrice \n2:searchForCompany'
selector = raw_input('enter 1 or 2: ')
if selector == '1':
    ticker = raw_input('enter ticker: ')
    print getCurrentPriceFromTicker(ticker)
elif selector == '2':
    ticker = raw_input('companyName: ')
    print searchForCompany(ticker)
