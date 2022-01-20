from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        data = list(jobs_reader)
        print(data)
    return data
    """Reads a file from a given path and returns its contents

# lê os dados
    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
