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
    arr = []
    with open(path, 'r', newline='') as file:
        # https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
        read = list(csv.DictReader(file))
        for row in read:
            arr.append(row)
    return arr
