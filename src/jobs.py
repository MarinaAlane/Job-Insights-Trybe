from functools import lru_cache
import csv


@lru_cache
def read(path):
    lista_vazia = []
    with open(path) as file:
        status_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for item in status_reader:
            lista_vazia.append(item)
    return lista_vazia
    # print(lista_vazia[0]["job_title"])
    # return list(csv.DictReader(file))


# read("jobs.csv")
