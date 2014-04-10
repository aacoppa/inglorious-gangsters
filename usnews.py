from bs4 import BeautifulSoup
import requests

for x in range(24):
    url = "http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+%d"%(x+1)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    name = soup.findAll("a", {"class":"school-name"})
    ranking = soup.findAll("span", {"class":"rankscore cluetip cluetip-stylized"})
    for y in range(11):
        try:
            print ranking[y][30:]
            print name[y].string
        except:
            pass
