from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_data = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = jobs_data
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
    return []
