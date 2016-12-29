import media
import fresh_tomatoes

# Creation of list of movies that are to be in the website.
toystory = media.Movie(
    "Toy Story",
    "Toy Story is an American computer-animated buddy-comedy adventure film",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie(
    "Avatar",
    "A marine on alien planet",
    "https://goo.gl/ZUxUOb",
    "https://www.youtube.com/watch?v=-9ceBgWV8io")

dear_zindagi = media.Movie(
    "Dear Zindagi",
    "An unconventional thinker (Shah Rukh Khan) helps a budding \
    cinematographer (Alia Bhatt) gain a new perspective on life.",
    "https://goo.gl/1ecVR5",
    "https://www.youtube.com/watch?v=2ZBPjt9NQtk")

school_of_rock = media.Movie(
    "School of Rock",
    "School of Rock is a comedy film about a struggling rock singer, \
    Dewey Finn (portrayed by Black), who is kicked out of his band \
    and subsequently disguises himself as a substitute teacher.",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie(
    "Ratatouille",
    "Ratatouille is a 2007 American computer-animated comedy film \
    and released by Walt Disney Pictures.",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

kirikParty = media.Movie(
    "Kirik Party",
    "Kirik Party is a 2016 Kannada comedy film \
    and released by Rakshit Shetty Pictures.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/1f/Kirik_Part_Poster.jpg/220px-Kirik_Part_Poster.jpg",
    "https://www.youtube.com/watch?v=IfvnbER_6sQ")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Midnight in Paris is an American 2011 romantic comedy fantasy film. \
    Set in Paris, the film follows Gil Pender, a screenwriter, \
    who is forced to confront the shortcomings of his relationship with\
    his materialistic fiancee and their divergent goals, which become \
    increasingly exaggerated as he travels back in time each night.",
    "http://tinyurl.com/7zebr4h",
    "https://www.youtube.com/watch?v=5nOF93SzX6s")

hunger_games = media.Movie(
    "Hunger Games",
    "The Hunger Games is a science fiction adventure film. \
    The story takes place in a dystopian post-apocalyptic \
    future in the nation of Panem, where boys and girls \
    between the ages of 12 and 18 must take part in the Hunger Games",
    "http://tinyurl.com/79m8ppm",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toystory, avatar, dear_zindagi, school_of_rock,
          ratatouille, midnight_in_paris, hunger_games, kirikParty]


# Calling open_movies_page definition from fresh_tomatoes library.
# This definition will create a static webpage for the list of movies
fresh_tomatoes.open_movies_page(movies)

# Use for testing.
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)
