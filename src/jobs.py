from functools import lru_cache
import csv


@lru_cache
def read(path):
    info = []
    with open(path, encoding="utf8", newline="") as file:
        data = csv.DictReader(file, delimiter=",", quotechar='"')
        for index in data:
            info.append(index)
    return info
