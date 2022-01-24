import csv

from functools import lru_cache


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
    with open(path, "r") as jobs_file:
        reader_file_jobs = csv.DictReader(jobs_file)
        content_data = list(reader_file_jobs)
    return content_data
