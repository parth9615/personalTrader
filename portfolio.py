import trader
import os
import sys
import re
import json
import datetime

"""
    This method takes the portfolio and saves it to a text file called
    info.txt to be read later when the program starts up again
"""
def saveToFile(dict):
    json.dump(dict, open("info.txt",'w'))



"""
    This method removes the file specifed from the computer
"""
def removeFileIfExists(name):
    path = os.getcwd() + "/" + name
    if os.path.exists(path):
        os.remove(path)


"""
    This method reads the file info.txt and saves all the portfolio information
    for all the users in an instance of portfolio
"""
def readFromFile():
    path = os.getcwd() + "/info.txt"
    if os.path.exists(path):
        d2 = json.load(open("info.txt"))
        if d2:
            return d2



"""
    This method takes a a key and value and adds it
    to the portfolio and formats it properly
"""
def addToPortfolio(key,value , portfolio):
    if key in portfolio:
        portfolio[key].append(value)
    else:
        ls = []
        ls.append(value)
        portfolio[key] = ls


"""
    This method makes sure that the result enterd is number
"""
def enterNumber(string):
    answer = raw_input(string)
    if answer.isdigit():
        return answer
    else:
        return enterNumber(string)


"""
    Returns a valid calendar year date
"""
def getDate(string):
    answer = raw_input(string)
    dateList = answer.split("-")
    if len(dateList) == 3:
        try:
            newDate = datetime.datetime(int(dateList[0]), int(dateList[1]), int(dateList[2]))
            return  answer
        except ValueError:
            return getDate(string)
    else:
        getDate(string)


"""
    This method adds work to the portfolio
"""
def portfolioManager(portfolio):
    while (True):
        name = raw_input("Enter Profile name: ")
        if name != 'quit':
            while(True):
                ticker = raw_input('enter ticker(quit to quit): ')
                quote = trader.getCurrentPriceFromTicker(ticker)
                if quote:
                    price = enterNumber("Enter price: ")
                    numbers = enterNumber("Enter quantity: ")
                    date = getDate("Enter date: (YYYY-MM-DD): ")
                    addToPortfolio(name , (trader.getCompanyName(ticker) , ticker, date, price, numbers) , portfolio )
                elif ticker != 'quit':
                    print 'wrong ticker try again'
                else:
                    break
        else:
            saveToFile(portfolio)
            break



"""
    List the portfolios names and their options and stocks
"""
def showPortfolio(portfolio):
    for item in portfolio:
        print item
        valueList = portfolio[item]
        for values in valueList:
            #trader.getCompanyName(ticker) , ticker, date, price, numbers
            print '\t company Name:      ' , values[0]
            print '\t\t stock Ticker:    ' , values[1]
            print '\t\t Date Purchased:  ' , values[2]
            print '\t\t Price Paid:      ' , values[3]
            print '\t\t Number of Stocks ' , values[4]
    print '\n\n'



"""
    This method returns the name of the company once the ticker is given
"""
"""
    Main runner method.
"""
def main():

    portfolio = readFromFile()
    if not portfolio:
        portfolio = {}

    while(True):
        option = raw_input('1: addToPortfolio\n2: showPortfolio\nEnter Choice:  ')
        if option == '1':
            portfolioManager(portfolio)
        elif option == '2':
            showPortfolio(portfolio)
        elif option == 'quit':
            break
        else:
            print '\n'




if __name__ == '__main__':
    main()
