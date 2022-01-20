import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = []
        for row in file_reader:
            jobs.append(row)
        return jobs
