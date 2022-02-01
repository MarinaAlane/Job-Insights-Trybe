from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs = []

    with open(path, mode="r") as file:

        jobs_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_csv:
            jobs.append(job)

    return jobs
