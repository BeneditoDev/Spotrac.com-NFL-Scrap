from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import csv
from getInfo import getPlayerInfo

def makeCsv(url):
    html = urlopen(url)
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
