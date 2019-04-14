class Movie():
    def __init__(self, title):
        self.title = title
        self.comparison = {}

    def like_more_than(self, other):
        if not isinstance(other, Movie):
            raise TypeError("other must be an instance of a Movie class")
        else:
            self.comparison[other.title] = True  # I like it more than other movie
            other.comparison[self.title] = False  # I like it less than other movie

    def __gt__(self, other):
        try:
            return self.comparison[other.title]
        except KeyError:
            return False

    def __lt__(self, other):
        try:
            return not self.comparison[other.title]
        except KeyError:
            return False
        
    def __str__(self):
        return 'Movie: ' + self.title
