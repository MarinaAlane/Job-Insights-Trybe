# https://python-forum.io/thread-9048.html
from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path) as file:
            jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            jobs = []
            for job in jobs_reader:
                jobs.append(job)
            return jobs
    except FileNotFoundError:
        print("file not found or corrupted")
