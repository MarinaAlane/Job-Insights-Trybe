from functools import lru_cache

import csv


@lru_cache
def read(path):
    content = []

    # o `enconding` foi uma dica postada pelo Erick Marinho
    # no canal da turma 11 no slack
    with open(path, 'r', encoding='iso-8859-1') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            content.append(row)

    return content
