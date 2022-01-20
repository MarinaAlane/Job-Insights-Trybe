from functools import lru_cache
import csv


@lru_cache
def read(path):
    rows = []
    with open(path, encoding="utf8", newline="") as file:
        csvreader = list(csv.DictReader(file))
        for row in csvreader:
            rows.append(row)
    return rows
