
import urllib2,json

def almanac(zip):
    url = "http://api.wunderground.com/api/4997e70515d4cbbd/almanac/q/%d.json"%(zip)
    r = urllib2.urlopen(url)
    data = json.loads(r.read())
    almanac = {"record low":data['almanac']['temp_low']['record']['F'].encode("ascii"),
               "record high":data['almanac']['temp_high']['record']['F'].encode("ascii"),
               "normal low":data['almanac']['temp_low']['normal']['F'].encode("ascii"),
               "normal high":data['almanac']['temp_high']['normal']['F'].encode("ascii")
               }
    return almanac


print(almanac(11214))
