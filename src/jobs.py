from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, "r") as file:
        file_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = file_reader

    file_row_list = []
    for row in data:
        row_dict = dict(zip(header, row))
        file_row_list.append(row_dict)

    """
    https://stackoverflow.com/questions/209840/how-do-i-convert-two-lists-into-a-dictionary
    
    Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    return file_row_list
