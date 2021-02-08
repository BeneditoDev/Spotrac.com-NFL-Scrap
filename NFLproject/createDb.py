#File to execute the scrap functions and allocate the data in a MySql Db.
#Run this file after "makeCsv" to get the players link database.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import csv
#Import funcion to get player salary data
from getInfo import getPlayerInfo
from makeHash import makeHash, veriHash

#Connecting to a DB in local host to store data.
db = MySQLdb.connect(host="localhost", user="python", passwd="admin", db="yourDB")
cursor = db.cursor()

try:
    f = open("final.txt", "r")
    start = f.read()
    if start == "":
        start = "0"
except:
    f = open("final.txt", "w")
    f.write("0")
    f = open("final.txt", "r")
    start = f.read()

#Creating tables, you can create them before running the code if you not will create the Db in one shot
if int(start) == 0:
    cursor.execute("CREATE TABLE players(cont int NOT NULL AUTO_INCREMENT, id varchar(10), firstN varchar(255), lastN varchar(255), team varchar(255), posi varchar(255), PRIMARY KEY (cont)) ENGINE=INNODB;")
    cursor.execute("CREATE TABLE salaries(cont int NOT NULL AUTO_INCREMENT, id varchar(255), capType varchar(255), a2020 varchar(255), a2021 varchar(255), a2022 varchar(255), a2023 varchar(255), a2024 varchar(255), a2025 varchar(255), a2026 varchar(255), a2027 varchar(255), a2028 varchar(255), a2029 varchar(255), a2030 varchar(255), a2031 varchar(255), PRIMARY KEY (cont)) ENGINE=INNODB;")
    control = 0
    loop = 0
else:
    pass
hashDb = {}
#Reading CSV created by "makeCsv.py" to get players links.
with open('dict.csv','r') as file:
    reader = csv.reader(file)
    line_count = 0
    loop = 0
    for row in reader:   
        if line_count < int(start) -1:
            line_count = line_count + 1
            pass
        else:
            url = row[1]

            capHit, deadCap, team, posi = getPlayerInfo(url)
            #Separating the First and second name.
            name = row[0].split()
                
            hashKey = makeHash(name[0], name[1], hashDb)
                
            #Parsing the names with problematic chars (names with ' and , cause bugs and errors in Mysql)
            if "'" in str(row[0]):
                row[0] = row[0].replace("'",'')
                name = row[0].split()
            if "’" in str(row[0]):
                row[0] = row[0].replace("’", '')
                name = row[0].split()        
            table_count = 1

            cursor.execute("INSERT INTO players(id, firstN, lastN, team, posi) VALUES('{0}','{1}', '{2}', '{3}', '{4}');".format( hashKey, name[0],name[1], team, posi))
            #In the salarie table create 2 rows per player hash, each one to store one aspect of the contract
            cursor.execute("INSERT INTO salaries(id, capType) VALUES('{0}','CapHit');".format(hashKey))
            cursor.execute("INSERT INTO salaries(id, capType) VALUES('{0}','DeadCap');".format(hashKey))
            table_count = table_count + 1
            for key, value in capHit.items():
                val = str(value)
                #Parsing the problematic characters;
                val = val.strip("[]").strip("''")
                if int(key) < 2020:
                    pass
                else:
                    year = "a" + key
                    cursor.execute("UPDATE salaries SET {0} = '{1}' WHERE id = '{2}' AND capType = 'CapHit';".format(year, val, hashKey))            

            for key2, value2 in deadCap.items():
                #Because a bug in the scrap of deadCap info, sometimes the function gets two deadCaps for one year (one of them is "0")
                if len(value2) > 1:
                    val2 = str(value2[0])
                else:
                    val2 = str(value2)
                    
                    val2 = val2.strip("[]").strip("''")
                if int(key2) < 2020:
                    pass
                else:
                    year2 = "a" + key2
                    cursor.execute("UPDATE salaries SET {0} = '{1}' WHERE capType = 'DeadCap'  AND id = '{2}';".format(year2, val2, hashKey))            
                        
            loop = loop +1
            line_count = line_count +   1
            print(line_count)
            if loop == 20:
                break
fw = open("final.txt", "w")
fw.write(str(line_count + 1))
db.commit()
db.close()                                                                                
