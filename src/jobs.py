from functools import lru_cache
import csv

# Desenvolvi este codigo tendo como base o PR do colega Luiz Wendell, que sanou
# algumas duvidas referentes a como criar a estrutura do arquivo. Pr do colega
# https://github.com/tryber/sd-011-project-job-insights/pull/3


@lru_cache
def read(path):
    jobs_list = []

    with open(path) as file:
        info_jobs = csv.reader(file)
        header, *data = info_jobs

        for row in data:
            new_dict = dict()
            for index in range(len(header)):
                new_dict[header[index]] = row[index]

            jobs_list.append(new_dict)

    return jobs_list
