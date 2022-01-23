from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path) as file:
            jobs_dict = csv.DictReader(file, delimiter=",", quotechar='"')
            jobs_list = []
            for job in jobs_dict:
                jobs_list.append(job)
            return jobs_list
# https://docs.python.org/pt-br/3/library/exceptions.html#bltin-exceptions
    except FileNotFoundError:
        print("File not found!!!")
