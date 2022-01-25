from functools import lru_cache
import csv

@lru_cache
def read(path):
    
    arr = []

    with open(path) as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs:
            arr.append(job)
   
    return arr
