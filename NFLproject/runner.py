from getInfo import getInfoNFL
from makeCsv import makeCsv
from getInfo import getInfoNFL
from makeHash import makeHash, veriHash
from createDb import createDB
from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import csv

def printMenu():
    print("")
    print("=====================================================================================================================")
    print("      To work correctly you need to create a MySQL database in the machine with a valid user before run option 2     ")
    print("=====================================================================================================================")
    print("")
    print("[1] | Make Csv.")
    print("[2] | Make a new base or continue an existing one.")
    choice = input("Answer:")
    if choice != '1' and choice != '2':
        printMenu()
    else:
        return choice


def op1():
    makeCsv("https://www.spotrac.com/nfl/contracts/sort-value/limit-2000/")

def op2():
    print("Configure a valid connection to an existing database")
    mydb = input("Choose the database to be used (The function will handle whether it is a new database or not): ")
    myhost = input("Mysql host: ")
    myuser = input("Mysql user: ")
    mypass = input("Mysql password: ")
    try:
        createDB(myhost, myuser, mypass, mydb)
    except:
        print("  ")
        print("Host, user, password, or database invalid.")
        print("  ")

def executeMenu():

    option = printMenu()

    if option == "1":
        op1()
        executeMenu()
    elif option == "2":
        op2()
        executeMenu()

executeMenu()
