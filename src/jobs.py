from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r", encoding="iso-8859-1") as file:
        read_file = csv.DictReader(file)
        dict_list = list(read_file)
    return dict_list
