from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, 'r') as file:
        jobs_list = []
        job_list = csv.DictReader(file)
        for job in job_list:
            jobs_list.append(job)

    return jobs_list


print(read("src/jobs.csv"))
