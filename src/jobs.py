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
        jobs_reader = csv.reader(file, delimiter=",", quotechar='"')
        headers, *data = jobs_reader

    lista = []

    for row in data:
        lista.append({headers[i]: row[i] for i in range(len(headers))})
    return lista
