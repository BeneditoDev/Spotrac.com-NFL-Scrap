from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import csv




def getPlayerInfo(url):
    html2 = urlopen(url)
    bsObj = BeautifulSoup(html2,"html.parser")
    #Get the position, the team  and the exp of teh player
    divMain = bsObj.find("div",{"id":"main"})
    divInfo = divMain.find("div",{"class":"player-info"})
    span = divInfo.find("span",{"class":"player-item position"})
    #span2 = divInfo.findAll("span",{"class":"player-infoitem"})[1]

    rawTeamPosi= span.get_text()
    #exp = span2.get_text()
    team_posi = rawTeamPosi.split(",")

 
    divFather = bsObj.find("div",{"class":"teams"})

    divSon = divFather.find("div",{"id":"current_contract"})
    body = divSon.table.find("tbody")
    trs = body.find_all("tr", class_="salaryRow")
    trCount = 0

    capHit = {}
    deadCap = {}
    for tr in range(len(trs)):

        tds = trs[tr].findAll("td")
        for td in range(len(tds)):
            if len(tds) > 5:
                #Year
                if 'href="http' in str(tds[td]):
                    key = tds[td].get_text()
                    capHit.setdefault(key, [])
                    deadCap.setdefault(key, [])
                #CapHit
                if 'salaryAmt result' in str(tds[td]):
                    si = tds[td].get_text()
                    si.strip
                    capHit[key].append(si.strip())
                #DeadCap
                if 'href="#"' in str(tds[td]):

                    if tds[td].get_text() == '':
                        deadCap[key].append(0)
                    else:
                        s = tds[td].get_text()
                        deadCap[key].append(s.strip())
        trCount = trCount + 1

    return capHit, deadCap, team_posi[0], team_posi[1]

url = "https://www.spotrac.com/nfl/baltimore-ravens/marlon-humphrey-21757/"
getPlayerInfo(url)
