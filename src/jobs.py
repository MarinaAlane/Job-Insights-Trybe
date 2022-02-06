from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        list_of_jobs = []

        # DictReader é um leitor a base de dicionários
        csv_content = csv.DictReader(file, delimiter=",", quotechar='"')

        for row in csv_content:
            list_of_jobs.append(row)
        # print(list_of_jobs)

        return list_of_jobs
