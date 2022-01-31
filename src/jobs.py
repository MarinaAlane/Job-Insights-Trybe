from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    with open(path, "r") as jobs_file_csv:
        jobs_list = [row for row in DictReader(jobs_file_csv)]
    return jobs_list
