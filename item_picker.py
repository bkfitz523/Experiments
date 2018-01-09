import argparse
import random


# Create list from file
def create_list(a_file):
    a_list = []
    with open(a_file) as f:
        for line in f:
            a_list.append(line)
    a_list = [x.strip() for x in a_list]
    return a_list


# Select 4 random values from item_array
def get_unique_items(choices, last):
    numbers = random.sample(range(0, last), choices)
    return numbers


# Print random items from a list
def print_selected_items(choices, selected_list):
    for x in range(len(choices)):
        selected = choices[x]
        print('{0}: {1}'.format(selected, selected_list[selected]))


# Arg Parser
parser = argparse.ArgumentParser()
parser.add_argument('-n', help='Number of items to select from a list')
parser.add_argument('-f', help='File with list of items')
args = parser.parse_args()
number_of_items = int(args.n)
if args.f is None:
    item_file = 'items.txt'
else:
    item_file = args.f

random_number = []
item_list = []
item_list = create_list(item_file)
last_index = len(item_list) - 1

if number_of_items is None:
    number_of_items = 3
elif number_of_items >= last_index:
    print('Selection larger than list size. Setting to max')
    number_of_items = last_index
else:
    number_of_items = number_of_items

random_number = get_unique_items(number_of_items, last_index)
print_selected_items(random_number, item_list)
