from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_data = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_insights = [job for job in jobs_data]

    return jobs_insights
