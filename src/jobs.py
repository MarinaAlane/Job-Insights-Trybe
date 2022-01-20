from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        path_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = path_reader
        table = []
        for row in data:
            # ..source: https://www.w3schools.com/python/ref_func_zip.asp
            collection = zip(header, row)
            table.append(dict(collection))
    return table
