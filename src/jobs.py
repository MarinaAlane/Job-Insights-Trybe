from functools import lru_cache
import csv


@lru_cache
def read(path):
    all_job_list = []

    with open(path) as file:
        jobs_infos = csv.DictReader(file, delimiter=",", quotechar='"')

        for job in jobs_infos:
            all_job_list.append(job)

    return all_job_list
