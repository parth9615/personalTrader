import trader
import os
import sys
import re
import json


"""
    This method takes the portfolio and saves it to a text file called
    info.txt to be read later when the program starts up again
"""
def saveToFile(dict):
    # removeFileIfExists('info.txt')
    # f = open('info.txt', 'a')
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
        else:
            return {}


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
    Main runner method.
"""
def main():
    portfolio = readFromFile()
    if portfolio:
        for item in portfolio:
            print item , portfolio[item]
    else:
        portfolio = {}
    while (True):
        name = raw_input("Enter Profile name: ")
        if name != 'quit':
            while(True):
                ticker = raw_input('enter ticker(quit to quit): ')
                quote = trader.getCurrentPriceFromTicker(ticker)
                if quote:
                    price = raw_input("Enter price: ")
                    numbers = raw_input("Enter quantity: ")
                    date = raw_input("Enter date: (YYYY-MM-DD): ")
                    addToPortfolio(name , (ticker, date, price, numbers) , portfolio )
                elif ticker != 'quit':
                    print 'wrong ticker try again'
                else:
                    break
        else:
            saveToFile(portfolio)
            break



if __name__ == '__main__':
    main()
