import urllib2
def get_state(zipcode):
    print zipcode
    if zipcode == 0:
        return "NA"
    url = "http://www.411.com/search/ReverseZip?wp_raz=%d" % (zipcode)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    req = urllib2.Request(url, headers=hdr)

    result = urllib2.urlopen(req)
    data = result.read()
    lines = data.split('\n')
    for line in lines:
        if "dfpSetTargetingParams['fst'] =" in line:
            return line[len(line)-4:len(line)-2]

#for i in range(0, 10):
#    print get_state(i * 10000 + 0011)
    

    
states = {
"Alabama" : "AL",
"Alaska" : "AK",
"Arizona" : "AZ",
"Arkansas" : "AR",
"California" : "CA",
"Colorado" : "CO",
"Connecticut" : "CT",
"Delaware" : "DE",
"Florida" : "FL",
"Georgia" : "GA",
"Hawaii" : "HI",
"Idaho" : "ID",
"Illinois" : "IL",
"Indiana" : "IN",
"Iowa" : "IA",
"Kansas" : "KS",
"Kentucky" : "KY",
"Louisiana" : "LA",
"Maine" : "ME",
"Maryland" : "MD",
"Massachusetts" : "MA",
"Michigan" : "MI",
"Minnesota" : "MN",
"Mississippi" : "MS",
"Missouri" : "MO",
"Montana" : "MT",
"Nebraska" : "NE",
"Nevada" : "NV",
"New Hampshire"   : "NH",
"New Jersey"      : "NJ",
"New Mexico"      : "NM",
"New York"        : "NY",
"North Carolina"  : "NC",
"North Dakota"    : "ND",
"Ohio" : "OH",
"Oklahoma" : "OK",
"Oregon" : "OR",
"Pennsylvania" : "PA",
"Rhode Island" :    "RI",
"South Carolina" :  "SC",
"South Dakota" :    "SD",
"Tennessee" : "TN",
"Texas" : "TX",
"Utah" : "UT",
"Vermont" : "VT",
"Virginia" : "VA",
"Washington" : "WA",
"West Virginia"   : "WV",
"Wisconsin" : "WI",
"Wyoming" : "WY",
}
locations = [
"North_east",
"East",
"West",
"South"
]

West = [
"MT",
"WY",
"CO",
"ID",
"UT",
"NE",
"AZ",
"CA",
"WA",
"HI",
"OR",
"AK",
]
North_east = [
"ME",
"RI",
"VT",
"NH",
"PA",
"NJ",
"NY",
"CI",
"MA",
]
South = [
"FL",
"GA",
"MD",
"KY",
"MI",
"TN",
"NC",
"SC",
"AL",
"AR",
"LA",
]
