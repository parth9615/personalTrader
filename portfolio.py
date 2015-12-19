import trader
import os
import sys
import re


def saveToFile(portfolio):
    f = open('info.txt', 'a')
    print portfolio
    for key in portfolio:
        string = key + ": " + str(portfolio[key]) + '\n'
        f.write(string)

def removeFileIfExists():
    path = os.getcwd() + "/info.txt"
    if os.path.exists(path):
        os.remove(path)

def readFromFile():
    f = open('read.txt' , 'rU')
    rawText = f.readlines()
    for x in rawText:
        y = x.split(":")
        itemList = removeCharacters(y[1])
        portfolio[y[0]] = itemList
    for x in portfolio:
        print x  , portfolio[x]



def removeCharacters(string):
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
