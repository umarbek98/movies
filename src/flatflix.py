class Movie:
    def __init__(self, title):
        pass

    def get_title(self):
        pass

    def get_reviews(self):
        pass

    def get_viewers(self):
        pass

    def average_rating(self):
        pass

    def highest_rating(self):
        pass


class Viewer:
    def __init__(self, username):
        pass

    def get_username(self):
        pass

    def get_reviews(self):
        pass

    def get_movies(self):
        pass

    def has_reviewed(self, movie):
        pass

    def rate_movie(self, rating):
        pass


class Review:
    def __init__(self, viewer, movie, rating):
        pass

    def get_rating(self):
        pass

    def get_viewer(self):
        pass

    def get_movie(self):
        pass
