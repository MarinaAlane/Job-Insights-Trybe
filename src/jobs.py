from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        return [job for job in jobs_reader]
