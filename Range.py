class Range():
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
    def in_range(self, n):
        """
            Checks if a value is in a range
        """
        return n >= self.bottom and n < self.top
    def below_range(self, n):
        """
            Checks if a value is below a range
        """
        return n < self.bottom

safety = Range(0, 10)
target = Range(10, 20)
reach = Range(20, 10000)



