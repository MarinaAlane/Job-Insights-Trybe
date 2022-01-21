from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        dict_jobs_reader = csv.DictReader(file)
        list_of_dict = list(dict_jobs_reader)
        return list_of_dict
