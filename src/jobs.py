from functools import lru_cache
import csv


@lru_cache
def read(path):
    result = []
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for val in content:
            result.append(val)
    return result
