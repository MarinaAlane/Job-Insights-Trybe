from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        header, *data = csv.reader(file, delimiter=",")
        fileDict = []
        for row in data:
            fileDict.append(dict(zip(header, row)))
    return fileDict
