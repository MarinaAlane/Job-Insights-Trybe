from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs = csv.DictReader(file)
        all_jobs = list(jobs)

    return all_jobs
