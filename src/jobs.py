from functools import lru_cache
import csv


# @lru_cache
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
    with open(path, "r") as file:
        csvFile = csv.reader(file, delimiter=',', quotechar='"')
        headers, *values = csvFile
        result = [{
            headers[index]: row[index] for index in range(len(row))
            } for row in values]
        return result


# print(read("./jobs.csv"))
