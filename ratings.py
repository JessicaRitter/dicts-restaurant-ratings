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
    user_restaurant_score = raw_input("Give it a score up to 5\n")

    restaurant_ratings_dict[user_restaurant] = user_restaurant_score
    ratings_in_order = sorted(restaurant_ratings_dict)

    for k in ratings_in_order:
        print k, "is rated at", restaurant_ratings_dict[k]


filename = sys.argv[1]
restaurant_ratings_dict = restaurant_rating_data(filename)
user_rating(restaurant_ratings_dict)