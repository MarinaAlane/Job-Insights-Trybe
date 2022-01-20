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
    result = []

    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = reader

        result = [
            {header[index]: row[index] for index, _ in enumerate(row)}
            for row in data
        ]

    return result


if __name__ == "__main__":
    print(read("src/jobs.csv")[0])
