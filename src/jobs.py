from functools import lru_cache
import csv


@lru_cache
def read(path):
    dicArray = []
    with open(path, 'r', newline='') as file:
        try:
            reader_file_cvs = list(csv.DictReader(file))
            for item in reader_file_cvs:
                dicArray.append(item)
        finally:
            return dicArray
