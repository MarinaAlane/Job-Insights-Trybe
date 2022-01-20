from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs_table = []
        for row in jobs_reader:
            jobs_table.append(row)
    return jobs_table
