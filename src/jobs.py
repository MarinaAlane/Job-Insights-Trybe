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
    result = []

    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        for thing in file_reader:
            result.append(thing)

    return result
