import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        result_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        lista = []
        for job in result_jobs:
            lista.append(job)
        return lista

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
    # return []
