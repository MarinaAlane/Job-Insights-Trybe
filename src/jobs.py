from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    with open(path, "r") as jobs_file:
        job_list = [row for row in DictReader(jobs_file)]
    return job_list
