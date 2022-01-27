from functools import lru_cache
import csv


@lru_cache
def read(path):
    lista_csv = None
    rows = []
    with open(path, newline='') as csvfile:
        lista_csv = csv.DictReader(csvfile)
        for row in lista_csv:
            rows.append(row)
    return rows
