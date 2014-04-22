class User():
    
    def __init__(self):
        self.uid = 0
        self.locations = []
        self.grades = {}
        self.sats = {}
        self.schools = []
    def add_location(self, place):
        self.locations.append(place)
    def add_grades(grades):
        for key in grades:
            self.grades[key] = grades[key]
    
