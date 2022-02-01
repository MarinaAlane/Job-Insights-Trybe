from functools import lru_cache
import csv


@lru_cache()
def read(path):
    with open(path) as file:
        file_content = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = file_content

        result_dicts = []
        for row in data:
            result_dicts.append(dict(zip(header, row)))

    return result_dicts
