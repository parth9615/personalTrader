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
    Main runner method.
"""
def main():
    portfolio = readFromFile()
    if not portfolio:
        portfolio = {}
    for item in portfolio:
        print item, portfolio[item]
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
