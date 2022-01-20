import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = csv_reader
        result = []
        for row in data:
            curr = dict()
            for i in range(len(header)):
                curr[header[i]] = row[i]
            result.append(curr)
    return result
