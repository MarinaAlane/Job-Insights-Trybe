from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        job_list = []
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_reader:
            job_list.append(job)
    return job_list
