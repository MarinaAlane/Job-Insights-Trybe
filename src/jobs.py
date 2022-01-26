import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, "r") as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')

        csv_list_dict = []

        for row in reader:
            csv_list_dict.append(row)

    return csv_list_dict
