from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    file_content_list = []

    with open(path) as file:
        file_content = DictReader(file, delimiter=",", quotechar='"')
        for row in file_content:
            file_content_list.append(row)

    return file_content_list
