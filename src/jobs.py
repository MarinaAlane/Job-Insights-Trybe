from functools import lru_cache
import csv


@lru_cache
def read(path):
    csvList = []
    with open(path, 'r', newline='') as file:
        try:
            read_file = list(csv.DictReader(file))
            for row in read_file:
                csvList.append(row)
        finally:
            print(csvList[0])
        return csvList
