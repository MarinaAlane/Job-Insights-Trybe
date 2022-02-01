from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        # DictReader cria uma lista de dicionarios,
        # usando as primeiras palavras separadas por "," como key
        jobs = csv.DictReader(file)

        # joblist = list(jobs)

        jobs_list = []
        for job in jobs:
            jobs_list.append(job)

    return jobs_list
