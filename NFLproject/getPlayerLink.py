from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb


html = urlopen("https://www.spotrac.com/nfl/contracts/sort-value/limit-2000/")
bsObj = BeautifulSoup(html,"html.parser")

divFather = bsObj.find("div",{"class":"team-content"})
divSon = divFather.find("div",{"id":"dataWrapper"})
body = divSon.find("tbody")
trs = body.findAll("tr")
names_links ={}
for player in range(len(trs)):
    anchor = trs[player].find("a",{"class":"team-name"})

    if 'href' in anchor.attrs:
        names_links[anchor.get_text()] = anchor.attrs['href'] 
 

f = open("example3.txt","a")


def getPlayerInfo(url):
    html2 = urlopen(url)
    bsObj = BeautifulSoup(html2,"html.parser")

    divFather = bsObj.find("div",{"class":"teams"})

    divSon = divFather.find("div",{"id":"current_contract"})
    body = divSon.table.find("tbody")
    trs = body.find_all("tr", class_="salaryRow")
    for row in trs:
        print(row)

url = "https://www.spotrac.com/nfl/kansas-city-chiefs/patrick-mahomes-21751/"
getPlayerInfo(url)
