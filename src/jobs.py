from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in file_reader:
            jobs_list.append(row)

    return jobs_list
