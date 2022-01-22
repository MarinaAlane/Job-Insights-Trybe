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
    teste = []

    with open(path) as file:
        jobs_list = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_list:
            teste.append(job)
    print(teste)

    return teste


read("src/jobs.csv")
