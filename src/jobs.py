from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as path_file:
        path_list = csv.DictReader(path_file)
        result = []
        for item in path_list:
            result.append(item)
    return result
