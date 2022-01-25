from functools import lru_cache
import csv

# ref: https://stackoverflow.com/a/50402818 (csv file to list of dictionaries)
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
    with open(path) as file:
        reader = csv.DictReader(file)
        a = list(reader)

    return a
