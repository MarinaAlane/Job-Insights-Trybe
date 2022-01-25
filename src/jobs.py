import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, "r") as file:
        jobs = csv.DictReader(file)
        jobs_list = list()
        for job in jobs:
            jobs_list.append(job)
        return jobs_list
