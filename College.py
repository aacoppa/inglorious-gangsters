class College:
    location_weight = 1.3
    sat_below_range_weight = 2
    sat_above_range_weight = 1.3
    gpa_below_weight = 2
    gpa_above_weight = 1.3
    rank_weight = .1
    def __init__(self, Location, Rank, Sat):
        self.location = Location 
        self.rank = Rank
        self.sats = Sats
    def get_comparison(User):
        """
            Returns value of comparison between User and School
        """
        compare_value = 0
        
        if location in User.locations:
            compare_value += location_weight
        
    def get_difficulty(User):
        """
            Returns the difficulty of getting into the school for for a User
        """
        difficulty = 0
        for subject in User.sats:
            difficulty += sat_range_conversion(User.sats[subject], subject)
        #difficulty += gpa_conversion(User.gpa)
        difficulty += sqrt(1000 - self.rank) / 10 * rank_weight 
    def sat_range_conversion(value, subject):
        """
            Converts SAT score to weighted difficulty value
        """
        if not subject in self.sats:
            return 0
        if self.sats[subject].in_range(value):
            return 0
        else if self.sats[subject].below_range(value):
            return -1 * sat_below_range_weight
        else:
            return 1 * sat_above_range_weight
    #def gpa_conversion(value):
    #    if value >= self.gpa
