from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import csv
from getInfo import getPlayerInfo

db = MySQLdb.connect(host="localhost", user="python", passwd="admin", db="yourDB")
cursor = db.cursor()



with open('dict.csv','r') as file:
    reader = csv.reader(file)
    loop = 0
    for row in reader:
        url = row[1]
        capHit, deadCap, team, posi = getPlayerInfo(url)
        name = row[0].split()
        #posi
        #firstName
        #lastName
        #team
        #capHit
        #deadCap
        
        '''
        if "'" in str(row[0]):
            row[0] = row[0].replace("'",'')
            name = row[0].split()
        if "’" in str(row[0]):
            row[0] = row[0].replace("’", '')
            name = row[0].split()

        cursor.execute("INSERT INTO players(firstN, lastN, team, posi) VALUES('{0}','{1}', '{2}', '{3}');".format(name[0],name[1], team, posi))
        '''
        loop = loop + 1
        print(loop)
        if loop == 10:
            break
        
db.commit()
db.close()