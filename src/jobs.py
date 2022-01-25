from functools import lru_cache
import csv


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
    all_job_list = []

    with open(path) as file:
        jobs_infos = csv.DictReader(file, delimiter=",", quotechar='"')

        for job in jobs_infos:
            all_job_list.append(job)

    return all_job_list
