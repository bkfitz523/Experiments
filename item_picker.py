import argparse
import modules


def validate_selection(choices, last):
    if choices is None:
        choices = 3
    elif choices >= last:
        print('Selection larger than list size. Setting to max')
        choices = last
    else:
        choices = choices
    return choices


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
item_list = modules.create_list(item_file)
last_index = len(item_list) - 1
number_of_items = validate_selection(number_of_items, last_index)
random_number = modules.get_unique_items(number_of_items, last_index)
print_selected_items(random_number, item_list)

'''
folder = 'download\\{0}'.format(folder_name)

    if not os.path.exists(folder):
        os.makedirs(folder)
'''