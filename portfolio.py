import trader
import os
import sys
import re

"""
    This method takes the portfolio and saves it to a text file called
    info.txt to be read later when the program starts up again
"""
def saveToFile(portfolio):
    removeFileIfExists('info.txt')
    f = open('info.txt', 'a')
    print portfolio
    for key in portfolio:
        string = key + ": " + str(portfolio[key]) + '\n'
        f.write(string)


"""
    This method removes the file specifed from the computer
"""
def removeFileIfExists(name):
    path = os.getcwd() + "/" + name
    if os.path.exists(path):
        os.remove(path)


""""
    This method reads the file info.txt and saves all the portfolio information
    for all the users in an instance of portfolio
""""
def readFromFile():
    f = open('read.txt' , 'rU')
    rawText = f.readlines()
    for x in rawText:
        y = x.split(":")
        portfolio[y[0]] = removeCharactersAndGetValues(y[1])


"""
    This method takes a  string and remvoes all the formatting from it and
    returns the stock infromation for the portfolio
"""
def removeCharactersAndGetValues(string):
    s1 = string.replace('[' , '')
    s2 = s1.replace(']' , '')
    s3 = s2.replace('(' , '')
    s4 = s3.replace("\n" , "")
    modified = s4.replace(')' , '')

    x = modified.split(",")
    tupList = []
    for a in range(len(x)/4):
        tupList.append(tuple(x[4*a: 4*(a+1)]))
    return tupList


""""
    This method takes a a key and value and adds it
    to the portfolio and formats it properly
""""
def addToPortfolio(key,value):
    if key in portfolio:
        portfolio[key].append(value)
    else:
        ls = []
        ls.append(value)
        portfolio[key] = ls


def main():
    while (True):
        name = raw_input("Enter Profile name: ")
        if name != 'quit':
            while(True):
                ticker = raw_input('enter ticker(quit to quit): ')
                # quote = trader.getCurrentPriceFromTicker(ticker)
                quote = "CHANGE THIS WHEN INTERNET CONNECTION"
                #if quote: RESTORE THIS WHEN INTERNET CONNECTION
                if ticker != 'quit':
                    price = raw_input("Enter price: ")
                    numbers = raw_input("Enter quantity: ")
                    date = raw_input("Enter date: (YYYY-MM-DD): ")
                    addToPortfolio(name , (ticker, date, price, numbers) )
                elif ticker != 'quit':
                    print 'wrong ticker try again'
                else:
                    break
        else:
            saveToFile(portfolio)
            break

portfolio = {}

if __name__ == '__main__':
  # removeFileIfExists()
  # main()
  readFromFile()
