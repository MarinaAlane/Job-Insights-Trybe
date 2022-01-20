from functools import lru_cache
import csv

# Para resolver esse requisito achei o método
# Zip que junta dois arrays criando um array de tuplas
# adicionei o método dict e transformei cada tupla em dicts

# https://realpython.com/python-zip-function/


# def zipDictTest():
#     numbers = [1, 2, 3]
#     letters = ['a', 'b', 'c']
#     numbers_and_letters = dict(zip(numbers, letters))
#     print(numbers_and_letters)


# zipDictTest()


@lru_cache
def read(path):
    result = []
    with open(path, "r") as file:
        jobs_csv = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = jobs_csv
        for row in data:
            result.append(dict(zip(header, row)))

    return result
