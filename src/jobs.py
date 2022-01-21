from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path) as file:
            jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            jobs = []
            for row in jobs_reader:
                jobs.append(row)
            return jobs
    except FileNotFoundError:
        print("arquivo inexistente")
