import random


# Create list from file
def create_list(a_file):
    a_list = []
    with open(a_file) as f:
        for line in f:
            a_list.append(line)
    a_list = [x.strip() for x in a_list]
    return a_list


# Select x random values from item_array
def get_unique_items(x, last):
    numbers = random.sample(range(0, last), x)
    return numbers