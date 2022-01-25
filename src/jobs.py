from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_list = csv.DictReader(file)
        jobs = []
        for item in jobs_list:
            jobs.append(item)
        return jobs