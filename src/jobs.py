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
    try:
        with open(path) as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
            if csv_reader:
                data = [*csv_reader]
            return data
    except (FileNotFoundError):
        print('Arquivo não encontrado')
        return None
