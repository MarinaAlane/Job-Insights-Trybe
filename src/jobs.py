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
    with open(path) as file:
        reader = csv.reader(file)
        header, *data = reader
        result = []
        for row in data:
            dict = {}
            for col in row:
                dict[header[row.index(col)]] = col
            result.append(dict)
    return result
