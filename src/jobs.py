from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path) as file:
            jobs = csv.DictReader(file)
            jobs_list = []
            for job in jobs:
                jobs_list.append(job)
            return jobs_list
    except FileNotFoundError:
        print('Por favor insira um arquivo válido')

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
