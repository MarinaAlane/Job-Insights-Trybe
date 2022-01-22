from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_dict = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_list = []
        for job in jobs_dict:
            jobs_list.append(job)
        return jobs_list
