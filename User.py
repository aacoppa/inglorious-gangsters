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
    def get_level(self):
        from College import sat_weight
        for subject in self.sats:
            return (self.sats[subject]) / 800.0 * sat_weight

            
    
