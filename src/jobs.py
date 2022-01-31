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
    jobs = []
    try:
        file = open(path)
    except OSError:
        print("arquivo inexistente")
    else:
        dicts = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in dicts:
            jobs.append(row)
        file.close()
    return jobs
