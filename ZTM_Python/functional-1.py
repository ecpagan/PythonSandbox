from functools import reduce

# 1 Capitalize all the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(text):
    return str(text).capitalize()


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(sorted(list(zip(my_strings, my_numbers)), key=lambda x: x[1]))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def scores_over_50(score_number):
    if score_number > 50:
        return score_number


print(list(filter(scores_over_50, scores)))

# 4 Combine all the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def combine_total(accumulator, item):
    return accumulator + item


print(reduce(combine_total, my_numbers + scores, 0))
