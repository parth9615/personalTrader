from termcolor import colored
import trader
import os
import sys
import re
import json
import datetime
import time
"""
    This method takes the portfolio and saves it to a text file called
    parth.txt to be read later when the program starts up again
"""
def saveToFile(dict):
    json.dump(dict, open("parth.txt",'w'))



"""
    This method removes the file specifed from the computer
"""
def removeFileIfExists(name):
    path = os.getcwd() + "/" + name
    if os.path.exists(path):
        os.remove(path)


"""
    This method reads the file parth.txt and saves all the portfolio information
    for all the users in an instance of portfolio
"""
def readFromFile():
    path = os.getcwd() + "/parth.txt"
    if os.path.exists(path):
        d2 = json.load(open("parth.txt"))
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
    if answer.replace('.','').replace('-','').isdigit():
        return float(answer)
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
    Returns red for negative
    green for positive
"""
def posOrNeg(first ,second):
    if first - second < 0:
        return 'red'
    else:
        return 'green'


"""
    Return white highlight if negative
    or return grey highlight if positive
"""
def posOrNegHighlight(first , second):
    if first - second < 0:
        return 'on_white'
    else:
        return 'on_grey'

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
                    addToPortfolio(name , (trader.getCompanyName(ticker) , ticker, date, price, numbers , numbers * price) , portfolio )
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
        print colored(item, 'grey' )
        valueList = portfolio[item]
        for values in valueList:
            current = float(trader.getCurrentPriceFromTicker(values[1]))
            currentTotal = float(current) * float(values[4])
            print colored('\t company Name:       ' , 'blue') , colored(values[0], 'green' , 'on_red')
            print colored('\t\t stock Ticker:     ' , 'blue') , values[1]
            print colored('\t\t Date Purchased:   ' , 'blue') , values[2]
            print colored('\t\t Number of Stocks  ' , 'blue') , values[4]
            print colored('\t\t Price Paid per:   ' , 'blue') , str(values[3]) + '\t' , colored('Current price:   ' , 'blue') , str(current) + '\t' , colored( current - float(values[3])   ,posOrNeg(current , float(values[3])) , posOrNegHighlight(current , float(values[3]) ), attrs=['bold'])
            print colored('\t\t Price Paid total: ' , 'blue') , str(values[5]) + '\t' , colored('Current price total: ' , 'blue') , str(currentTotal) + '\t' , colored(currentTotal - float(values[5])  ,posOrNeg(currentTotal , float(values[5]) ), posOrNegHighlight(currentTotal , float(values[5]) ), attrs=['bold'])


def searchForCompanies():
    ticker = raw_input("Enter company: ")
    trader.searchForCompany(ticker)


"""
    Showing the real time profit loss for each statement
"""
def showRealTime(portfolio):
    while(True):
        print colored('PRESS CONTROL C TO EXIT' , 'red' , attrs=['bold'])
        for item in portfolio:
            print colored(item, 'grey' )
            valueList = portfolio[item]
            for values in valueList:
                currentTotal = float(trader.getCurrentPriceFromTicker(values[1])) * float(values[4])
                print '\t' , values[0] , colored(float(values[5]) - currentTotal ,posOrNeg(float(values[5]) , currentTotal), posOrNegHighlight(float(values[5]) , currentTotal), attrs=['bold'])
        time.sleep(10)
        os.system('clear')

"""
    Main runner method.
"""
def main():

    portfolio = readFromFile()
    if not portfolio:
        portfolio = {}

    while(True):
        option = raw_input('1: addToPortfolio\n2: showPortfolio\n3: Real Time profit loss\n4: Search for companies\nEnter Choice:  ')
        if option == '1':
            portfolioManager(portfolio)
        elif option == '2':
            showPortfolio(portfolio)
        elif option == '3':
            showRealTime(portfolio)
        elif option == '4':
            searchForCompanies()
        elif option == 'quit':
            break
        else:
            print '\n'




if __name__ == '__main__':
    main()
