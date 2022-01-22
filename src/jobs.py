from functools import lru_cache
import csv

@lru_cache
def read(path):
    my_list = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            my_list.append(row)
    
    return my_list
