from functools import lru_cache
import csv

# referencia do codigo:
# https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries/46969915


@lru_cache
def read(path):
    list_jobs = []
    with open(path, "r", encoding="utf8") as file:
        jobs_result = csv.DictReader(file, delimiter=",")
        for row in jobs_result:
            list_jobs.append(row)
    return list_jobs
