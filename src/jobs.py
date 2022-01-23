from functools import lru_cache
import csv

jobs_list = []


@lru_cache
def read(path):
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in file_reader:
            jobs_list.append(row)

    return len(jobs_list)
