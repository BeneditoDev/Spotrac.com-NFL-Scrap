from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb


html = urlopen("https://www.spotrac.com/nfl/contracts/sort-value/limit-2000/")
bsObj = BeautifulSoup(html,"html.parser")

divFather = bsObj.find("div",{"class":"team-content"})
divSon = divFather.find("div",{"id":"dataWrapper"})