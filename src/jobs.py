from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csv_file:
        jobs_file = csv.DictReader(csv_file, delimiter=",", quotechar='"')
        jobs = []
        for index in jobs_file:
            jobs.append(index)
    return jobs


# read('jobs.csv')
