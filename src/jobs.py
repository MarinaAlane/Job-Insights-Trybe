from functools import lru_cache
import csv


@lru_cache
def read(path):
    # obrigada pessoas da turma 03 e 04 que postaram o erro exception
    # UnicodeDecodeError no slack e como resolver <3
    with open(path, encoding='utf-8') as file:
        jobs_list = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = jobs_list

        result = []

        for row in data:
            row = dict(zip(header, row))
            result.append(row)
        return result
