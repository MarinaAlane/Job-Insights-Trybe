from functools import lru_cache
import csv #importa csv para poder ler os dados

@lru_cache
def read(path):
    list = []
    with open(path) as job_file:
        job_list = csv.DictReader(job_file)
    for job in job_list:
        list.append(job)
   
    return list
