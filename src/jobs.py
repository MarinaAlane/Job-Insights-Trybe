from functools import lru_cache
import pandas as pd
import json


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
    file = pd.read_csv(path, dtype=str, index_col=False)
    chaves = file.columns
    result = []
    for _, row in file.iterrows():
        result.append({chave: row[chave] for chave in chaves})
    return result
