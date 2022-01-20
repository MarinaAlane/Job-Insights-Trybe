from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_dict_list = []
        for row in jobs_reader:
            jobs_dict_list.append(row)

    return jobs_dict_list
