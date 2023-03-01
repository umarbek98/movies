from src.flatflix import Movie, Review, Viewer


def test_viewer_init_username():
    """
    Should be able to initialize a viewer with
    a username
    """
    viewer = Viewer('user123')
    assert viewer.username == 'user123'

def test_viewer_get_username():
    """
    get_username() should return the username of
    the viewer
    """
    viewer = Viewer('user123')
    assert viewer.get_username() == 'user123'

def test_viewer_get_reviews():
    """
    get_reviews() should return the list of reviews
    associated with the viewer
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    viewer.reviews = [review]
    assert viewer.get_reviews() == [review]

def test_viewer_get_movies():
    """
    get_movies() should return the list of movies
    associated with the viewer
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    viewer.reviews = [review]
    assert viewer.get_movies() == [movie]

def test_viewer_rate_movie():
    """
    rate_movie(movie, rating) should create a new review
    object and attach it to the viewer
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    viewer.rate_movie(movie, 5)
    assert len(viewer.reviews) == 1
    assert viewer.reviews[0].rating == 5


def test_viewer_has_reviewed():
    """
    has_reviewed(movie) should return True if the
    viewer has reviewed this movie
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    viewer.reviews = [review]
    assert viewer.has_reviewed(movie) == True
