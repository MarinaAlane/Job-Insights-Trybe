from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_csv = csv.reader(file, delimiter=",", quotechar='"')
        header, *rows = jobs_csv

    # Para usar o .zip eu lembrei do platao das 13:00 de 20/01/2022
    # e tambem consultei este artigo em RealPython para converter de HEX para Humanos
    # https://realpython.com/python-zip-function/
    content = []
    for row in rows:
        row = dict(zip(header, row))
        content.append(row)
    print(content[0])
    return content
