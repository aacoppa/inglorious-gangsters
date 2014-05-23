from bs4 import BeautifulSoup
import requests,urllib2,json

def almanac(zip):
    url = "http://api.wunderground.com/api/4997e70515d4cbbd/almanac/q/%d.json"%(zip)
    r = urllib2.urlopen(url)
    data = json.loads(r.read())
    print data['almanac']


almanac(11214)
