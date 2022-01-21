from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        status_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        data_content = list(status_reader)
    return data_content
