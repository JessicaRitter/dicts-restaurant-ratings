"""Restaurant rating lister."""
import sys

def restaurant_rating_data(filename):
    opened_file = open(filename)
    restaurant_ratings_dict = {}

    for line in opened_file:
        restaurant_info = line.split(":")
        restaurant_ratings_dict[restaurant_info[0]] = restaurant_info[1].rstrip()

    return restaurant_ratings_dict


# restaurant_rating_data("scores.txt")
def user_rating(restaurant_ratings_dict):
    user_restaurant = raw_input("What restaurant do you want to rate?\n")
    # user_restaurant_score = raw_input("Give it a score (between 1 and 5)\n")
    user_restaurant_score = None

    while user_restaurant_score is None or user_restaurant_score not in range(5):
        user_restaurant_score = int(raw_input("Give it a score (between 1 and 5)\n"))
        if user_restaurant_score in range(5):
            restaurant_ratings_dict[user_restaurant] = user_restaurant_score
        else:
            print "Try again, that's not a number between 1 and 5"

    ratings_in_order = sorted(restaurant_ratings_dict)

    for k in ratings_in_order:
        print k, "is rated at", restaurant_ratings_dict[k]


filename = sys.argv[1]
restaurant_ratings_dict = restaurant_rating_data(filename)
user_rating(restaurant_ratings_dict)