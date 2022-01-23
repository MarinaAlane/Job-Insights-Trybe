from functools import lru_cache
import csv


@lru_cache(maxsize=None)
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
        jobs = csv.DictReader(file)  # retorna lista de tuples
        return [dict(row) for row in jobs]  # dict() cria um dicionario e
        # itera nos tuples, pegando primeiro valor como chave e o segundo como
        # value
