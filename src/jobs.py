from functools import lru_cache
import csv

@lru_cache
def read(path):
    arrTeste = []
    with open(path, 'r', newline='') as file:
        try:
            read_file = list(csv.DictReader(file))
            for row in read_file:
                arrTeste.append(row)
        finally:
            print(arrTeste[0])
    return arrTeste
