from functools import lru_cache
import csv


@lru_cache
def read(path):
    arrary = []
    with open(path, 'r', newline='') as file:
        try:
            view_file = list(csv.DictReader(file))
            for row in view_file:
                arrary.append(row)
        finally:
            return arrary
