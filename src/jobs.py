from functools import lru_cache

import csv


@lru_cache
def read(path):
    with open(path) as file:
        job_file = csv.DictReader(file)
        jobs_list = []
        for job in job_file:
            jobs_list.append(job)
        return jobs_list
