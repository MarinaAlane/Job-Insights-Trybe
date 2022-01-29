from functools import lru_cache
import csv


@lru_cache
def read(path):

    lista = []
    with open(path) as file:
        list = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in list:
            lista.append(row)

    return lista
