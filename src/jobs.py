from functools import lru_cache
import csv


@lru_cache
def read(path):
    rows = []
    with open(path, encoding="utf8", newline="") as file:
        csv_reader = list(csv.DictReader(file))
        for row in csv_reader:
            rows.append(row)
    return rows
