from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as f:
        return list(csv.DictReader(f))
