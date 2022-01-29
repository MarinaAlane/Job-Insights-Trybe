from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        csv_dict = []
        csv_readed = csv.DictReader(file, delimiter=",", quotechar='"')
        for item in csv_readed:
            csv_dict.append(item)

    return csv_dict
