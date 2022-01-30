from functools import lru_cache
import csv


@lru_cache(maxsize=None)
def read(path):
    with open(path) as file:
        return list(csv.DictReader(file, delimiter=",", quotechar='"'))
