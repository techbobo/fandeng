# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import json
import re
from datetime import datetime
from pprint import pprint
from urllib.request import urlretrieve

FAN_DENG_RESPONSE = '/Users/bobo/Desktop/fandeng/response/'
FAN_DENG_DOWNLOAD = '/Users/bobo/Desktop/fandeng/download/'


def download_book(book):
    book_name = book['bookName']
    book_author_name = book['bookAuthorName']
    book_micro_timestamp = book['lastUpdateTime']
    book_date = datetime.fromtimestamp(book_micro_timestamp / 1000).strftime('%Y%m%d')
    book_media_url = book['mediaUrls'][0]
    download_filename = book_date + '_' + book_name + '_' + book_author_name + '.mp3'
    download_filename = re.sub(r"[\/\\\:\*\?\"\<\>\|]", '_', download_filename)
    download_filepath = FAN_DENG_DOWNLOAD + download_filename
    print('Download url: ' + book_media_url)
    print(download_filename + ' downloading...')
    response = urlretrieve(book_media_url, download_filepath)
    print(response)
    print(download_filename + ' done!!!')


def parse_file(file_path):
    print('============================================================')
    print('Parse ' + file_path)
    f = open(file_path, 'r')
    content = f.readline()
    response = json.loads(content)
    book = response['data']
    download_book(book)
    f.close()
    os.remove(file_path)


def loop_files(dirPath):
    file_names = os.listdir(dirPath)
    for file_name in file_names:
        file_path = dirPath + file_name
        parse_file(file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loop_files(FAN_DENG_RESPONSE)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
