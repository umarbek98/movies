from src.flatflix import Movie, Review, Viewer


def test_movie_init_title():
    """
    Should be able to initialize a movie object
    with a title
    """
    movie = Movie("Cocaine Bear")
    assert movie.title == "Cocaine Bear"

def test_movie_get_title():
    """
    get_title() should return the title of the movie
    """
    movie = Movie("Cocaine Bear")
    assert movie.get_title() == "Cocaine Bear"

def test_movie_get_reviews():
    """
    get_reviews() should return the list of reviews
    associated with the movie
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    movie.reviews = [review]
    assert movie.get_reviews() == [review]

def test_movie_get_viewers():
    """
    get_viewers() should return the list of viewers
    associated with the movie
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    movie.reviews = [review]
    assert movie.get_viewers() == [viewer]

def test_movie_average_rating():
    """
    average_rating() should return the average 
    rating for the movie
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    movie.reviews = [review]
    assert movie.average_rating() == 5

def test_movie_highest_review():
    """
    highest_review() should return the rating object
    with the highest rating
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review_high = Review(viewer, movie, 5)
    review_low = Review(viewer, movie, 1)
    movie.reviews = [review_high, review_low]
    assert movie.highest_review() == review_high
