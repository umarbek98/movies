from src.flatflix import Movie, Review, Viewer


def test_review_init_viewer_movie_rating():
    """
    Should be able to initialize a review object with
    a viewer, movie, and rating
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    assert review.rating == 5
    assert review.viewer == viewer
    assert review.movie == movie

def test_review_get_rating():
    """
    get_rating() should return the rating for the review
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    assert review.rating == 5

def test_review_get_viewer():
    """
    get_viewer() should return the viewer associated
    with the review
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    assert review.get_viewer() == viewer

def test_review_get_movie():
    """
    get_movie() should return the movie associated
    with the review
    """
    movie = Movie("Cocaine Bear")
    viewer = Viewer('user123')
    review = Review(viewer, movie, 5)
    assert review.get_movie() == movie
