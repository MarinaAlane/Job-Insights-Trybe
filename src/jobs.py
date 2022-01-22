from functools import lru_cache
import csv


@lru_cache()
def read(path):
    with open(path) as file:
        file_content = list(csv.reader(file))
        header, *data = file_content

        list_of_dicts = []

        for row in data:
            new_dict = dict()
            for i in range(len(row)):
                new_dict[header[i]] = row[i]
            list_of_dicts.append(new_dict)

        return list_of_dicts
