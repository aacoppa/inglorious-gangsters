class User():
    
    def __init__(self):
        self.uid = 0
        self.locations = []
        self.grades = {}
        self.sats = {}
    def addLocation(self, place):
        self.locations.append(place)
