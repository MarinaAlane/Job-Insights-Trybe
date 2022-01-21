import csv
from functools import lru_cache


@lru_cache
def read(path):
    new_arr = []
    with open(path, 'r', newline='') as file:
        # Solution resolved based on src:
        # https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
        read_file = list(csv.DictReader(file))
        for row in read_file:
            new_arr.append(row)
    return new_arr
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
    # return []
