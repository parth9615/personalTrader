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
    for key in portfolio:
        string = getValueToWrite(key, portfolio[key][0])
        f.write(string)

"""
    This method takes the key and value from the portfolio
    and converts the value in a consitent format for the
    the files to do i/o
"""
def getValueToWrite(key, value):
    strList = key + ' : '
    for i in range(len(value) - 1):
        strList += ' ' + value[i] + ' , '
    strList+= ' ' + value[i+1] + '\n'
    return strList

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
        f = open('info.txt' , 'rU')
        rawText = f.readlines()
        for x in rawText:
            y = x.split(":")
            portfolio[y[0]] = removeCharactersAndGetValues(y[1])


"""
    This method takes a  string and remvoes all the formatting from it and
    returns the stock infromation for the portfolio
"""
def removeCharactersAndGetValues(value):
    string = value.replace(" " , "")
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


"""
    This method takes a a key and value and adds it
    to the portfolio and formats it properly
"""
def addToPortfolio(key,value):
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
    readFromFile()
    for item in portfolio:
        print item , portfolio[item]
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
    main()
