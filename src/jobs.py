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
    with open(path, 'r') as file:
        result = []
        content = csv.reader(file, delimiter=",", quotechar='"')
        header, *data_list = content
        for data in data_list:
            job = dict()
            for column in header:
                job.update({column: data[header.index(column)]})
            result.append(job)
        return result
