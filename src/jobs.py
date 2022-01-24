from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_from_csv = csv.DictReader(file)
        jobs = []
        for row in jobs_from_csv:
            jobs.append(row)
        return jobs
