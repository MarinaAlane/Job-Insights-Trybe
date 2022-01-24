import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, mode="r") as file:
        jobs_reader = csv.reader(file, delimiter=",", quotechar='"')

        header, *datas = jobs_reader

        jobs = [dict(zip(header, data)) for data in datas]

    return jobs
