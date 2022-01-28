import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_by_title = []
        for row in jobs_reader:
            new_title = {}
            title = row["job_title"]
            new_title["job_title"] = title
            jobs_by_title.append(new_title)
        return print(jobs_by_title)
