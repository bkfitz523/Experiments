import argparse
import modules
import os, sys
import urllib.request as url_download

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='File with list of items')
args = parser.parse_args()
if args.f is None:
    item_file = 'download.txt'
else:
    item_file = args.f


def download_list_of_items(list_of_items, folder, base_name, digits):
    # list
    # path

    if not os.path.exists(folder):
        os.makedirs(folder)

    last_index = len(list_of_items)

    for x in range(0, last_index):
        num = str(x).zfill(digits)
        print("Downloading Item "+num)
        url_download.urlretrieve(list_of_items[x], folder + base_name + num + ".jpg")


download_items = modules.create_list(item_file)
# path = "download\\cw"
# print(download_items[0])
# url_download.urlretrieve(download_items[0], path + "\\cw_01.jpg")

download_list_of_items(
    list_of_items=download_items,
    folder="download\\mm_rs\\",
    base_name="mm_rs_01_",
    digits=2
)

print('Completed')
sys.exit(0)
