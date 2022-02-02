import csv
from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    jobs = []
    with open(path) as file:
        job_list = csv.DictReader(file)
        for job in job_list:
            jobs.append(job)
    return jobs
