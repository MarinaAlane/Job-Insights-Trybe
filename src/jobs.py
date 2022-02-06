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
# python3 -m pytest tests/test_jobs.py
# https://betterprogramming.pub/how-to-pretty-print-in-python-9b1d8764d151#:~:text=stream%20(None)%20%3A%20When%20you,when%20specific%20formatting%20is%20needed.
