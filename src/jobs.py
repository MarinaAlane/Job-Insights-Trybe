from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as jobs:
        jobs_list = csv.DictReader(jobs)
        return list(jobs_list)
