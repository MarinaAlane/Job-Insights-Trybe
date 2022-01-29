from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path) as file:
        info_jobs = csv.DictReader(file, delimiter=",", quotechar='"')

        jobs = []
        for job in info_jobs:
            jobs.append(job)
    return jobs
