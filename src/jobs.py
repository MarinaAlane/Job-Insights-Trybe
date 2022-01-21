from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        list = [data for data in csv.DictReader(file, delimiter=",")]
    return list
