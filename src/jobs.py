from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        status_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for item in status_reader:
            print(list(item))
            break
    return []


read("jobs.csv")
