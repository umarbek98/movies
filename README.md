# Object Relations Code Challenge - Flatflix

For this challenge, we'll be working with a Movie Review domain, like Netflix.

We have three models: `Viewer`, `Movie`, and `Review`.

A `Movie` has many `Review`s. A `Viewer` has many `Review`s. A `Review` belongs to a `Viewer` and belongs to a `Movie`.

`Viewer` - `Movie` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge does not have tests. You cannot run `pytest`. You'll need to create your own sample instances so that you can try out your code on your own. Make sure your relationships and methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it, run `python tools/debug.py` from the command line. This will start a `ipdb` session with your classes defined. You can test out the methods that you write here. You can add code to the `tools/debug.py` file to define variables and create sample instances of your objects.

Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

### Initializers, Readers, and Writers

#### Movie

- `Movie __init__(self, title)`
  - `Movie` is initialized with a title (string)
- `Movie get_title()`
  - returns the `Movie`'s title

#### Viewer

- `Viewer __init__(self, username)`
  - `Viewer` is initialized with a username (string)
- `Viewer get_username()`
  - returns the Viewer's username

#### Review

- `Review __init__(self, viewer, movie, rating)`
  - `Review` is initialized with a `Viewer` instance, a `Movie` instance, and a rating (int)
- `Review get_rating()`
  - returns the rating for the `Review` instance

### Object Relationship Methods

#### Review

- `Review get_viewer()`
  - returns the `Viewer` instance associated with the `Review` instance
- `Review get_movie()`
  - returns the `Movie` instance associated with the `Review` instance

#### Viewer

- `Viewer get_reviews()`
  - returns a list of `Review` instances associated with the `Viewer` instance.
- `Viewer get_movies()`
  - returns a list of `Movie` instances reviewed by the `Viewer` instance.

#### Movie

- `Movie get_reviews()`
  - returns a list of all the `Review` instances for the `Movie`.
- `Movie get_viewers()`
  - returns a list of all of the `Viewer` instances that reviewed the `Movie`.
  - HINT: you can get the viewers by iterating through the list of reviews

### Aggregate and Association Methods

#### Viewer

- `Viewer has_reviewed(movie)`
  - returns `true` if the `Viewer` has reviewed this `Movie` (if there is a `Review` instance that has this `Viewer` and `Movie`), returns `false` otherwise
- `Viewer rate_movie(movie, rating)`
  - a `Movie` instance and a rating (int) are passed in as arguments
  - this method should create a new `Review` instance and attach it to the `Viewer` instance

#### Movie

- `Movie average_rating()`
  - returns the average of all ratings for the `Movie` instance
  - to average ratings, add all ratings together and divide by the total number of ratings.
- `Movie highest_rating()` 
  - returns the `Review` instance with the highest average rating.
