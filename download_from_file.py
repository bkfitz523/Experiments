import argparse
import modules
import os
import urllib.request as url_request


parser = argparse.ArgumentParser()
parser.add_argument('-f', help='File with list of items')
args = parser.parse_args()
if args.f is None:
    item_file = 'download.txt'
else:
    item_file = args.f


def download_from_file(folder_name, url, length, img_name, digits):
    # Create directory if does not exist

    folder = 'download\\{0}'.format(folder_name)

    if not os.path.exists(folder):
        os.makedirs(folder)

    # Loop to download images
    for x in range(0, length):
        num = str(x).zfill(digits)
        img_url = url[x].format(num)
        img_name
        try:
            print(img_url.format(num))
            print(img_name.format(num))
            url_request.urlretrieve(img_url, folder + '\\' + img_name.format(num))
        except:
            print('Not found. Continuing to next item...')
            continue


download_items = modules.create_list(item_file)
list_size = len(download_items) #- 1

download_from_file(
    folder_name='Pokemon',
    url=download_items,
    length=list_size,
    img_name='pokemon',
    digits=3
)