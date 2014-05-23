from User import User
from locations import get_state
import math

location_weight = 1.3
sat_below_range_weight = 2
sat_above_range_weight = 1.3
sat_weight = 1.3
gpa_below_weight = 2
gpa_above_weight = 1.3
rank_weight = .1
class College:
    
    def __init__(self, name, location, rank, sats, size, tuition, address, zipcode):
        self.name = name
        self.location = location 
        self.rank = rank
        self.sats = sats
        self.tuition = tuition
        self.size = size
        self.address = address
        self.state = get_state(zipcode)
    def get_difficulty_comparison(self, user_level):
        """
            returns value of comparison between user and school
        """
        compare_value = 0
        
        college_level = self.get_difficulty()
        
        total_value = user_level + college_level
        return total_value
    def get_compatability(self, User):
        """
            Find out how much this college is applicable to the user
        """
        compatabilty = 0
        for state in User.states:
            if self.state == state:
                compatabilty += .5
        #Location check; ie Northeast or south
        for location in User.locations:
            if self.state in Area[location]:
                compatabilty += .3
        for temp in User.temperatures.keys():
            if self.temperature - 10 < temp and self.temperature + 10 > temp:
                   compatabilty += User.temperatures[temp]
                   break
        return compatabilty
    def find_location(self):
        key = "AIzaSyAKd5dbb90Go0U3YNo4veBil91D0u2DBio"
        url = "https://maps.googleapis.com/maps/api/place/autocomplete/xml?input={0}&sensor=false&key={1}".format(self.name.replace(" ", "&"), key)
        result = urllib2.urlopen(url).read()
        print result
        exit()
    def get_difficulty(self):
        """
            returns the difficulty of getting into the school for for a user
        """
        difficulty = 0.0
        difficulty -= (300 - self.rank) / 300.0
        if not self.sats:
            return difficulty
        for subject in self.sats:
            difficulty += self.sat_range_conversion(subject)
        return difficulty
    def sat_range_conversion(self, subject):
        """
            Converts SAT score to weighted difficulty value
        """
        if not self.sats or not subject in self.sats:
            return .5
        return (self.sats[subject].bottom + self.sats[subject].top) / 1600 * sat_weight
    def print_college(self):
        print self.name
        if not self.sats:
            print "%s, no SAT data available" % (self.name)
        else:
            print "{0} Math {1}-{2} Reading {3}-{4}".format("Sats", self.sats['math'].bottom,
                  self.sats['math'].top, self.sats['reading'].bottom, self.sats['reading'].top)
        print "Size: {0} Tuition: {1} State: {2}".format(self.size, self.tuition, self.state)


    #def gpa_conversion(value):
    #    if value >= self.gpa

