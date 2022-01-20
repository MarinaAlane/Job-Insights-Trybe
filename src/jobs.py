from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
