from functools import lru_cache
import csv


@lru_cache
def read(path):
    result = []
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_reader:
            result.append(job)

    return result
