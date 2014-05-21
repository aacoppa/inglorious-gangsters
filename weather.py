from bs4 import BeautifulSoup
import requests

def almanac(zip):
    url = "http://api.wunderground.com/api/4997e70515d4cbbd/almanac/q/%d.json"%(zip)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    print soup.findAll("almanac")


almanac(11214)
