from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_data = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = []
        for job in jobs_data:
            jobs.append(job)
        return jobs
