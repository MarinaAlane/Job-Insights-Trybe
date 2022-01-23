from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_title = csv.DictReader(file, delimiter=',', quotechar='"')
        jobs = []
        for job in jobs_title:
            jobs.append(job)
        return jobs
