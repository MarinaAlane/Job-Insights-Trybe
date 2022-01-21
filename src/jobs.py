from functools import lru_cache

import csv


@lru_cache
def read(path):
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
