import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_list = []
        for row in jobs_reader:
            new_job = {}
            for key, value in row.items():
                new_job[key] = value
            jobs_list.append(new_job)
        return jobs_list

# read("src/jobs.csv")
