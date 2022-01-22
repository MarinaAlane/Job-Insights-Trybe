from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        dicts_from_csv = csv.DictReader(file, delimiter=",", quotechar='"')

        list_of_dicts = []
        for row in dicts_from_csv:
            list_of_dicts.append(row)

    return list_of_dicts
