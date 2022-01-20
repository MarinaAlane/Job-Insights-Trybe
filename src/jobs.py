from functools import lru_cache

import csv


@lru_cache
def read(path):
    content = []

    with open(path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            content.append(row)

    return content
