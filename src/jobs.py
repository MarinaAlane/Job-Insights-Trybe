from functools import lru_cache
import csv


# https://docs.python.org/3/library/csv.html
# Uso do zip: plantão do dia 20 sobre estruturas de Dados e List Comprehension
# ainda bem que tirei print para estudar!!!!
# DICT-ZIP: https://pythonacademy.com.br/blog/dicts-ou-dicionarios-no-python
# ZIP: http://devfuria.com.br/python/built-in-zip/
# ZIP: https://pythonhelp.wordpress.com/2013/04/16/funcao-zip-em-python/
@lru_cache
def read(path):
    with open(path, newline='') as file:
        reader_file = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = reader_file
        jobs = []
        for row in data:
            row = dict(zip(header, row))
            jobs.append(row)
        return jobs
