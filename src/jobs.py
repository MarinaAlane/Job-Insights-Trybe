import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, 'r') as f:
        csv_reader = csv.DictReader(f)
        return [row for row in csv_reader]
