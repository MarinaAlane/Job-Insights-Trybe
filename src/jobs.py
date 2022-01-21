import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        content = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = content

    jobs_list = []
    for row in data:
        jobs_dict = {}
        for index in range(0, len(row)):
            jobs_dict[header[index]] = row[index]
        jobs_list.append(jobs_dict)
    return jobs_list


if __name__ == "__main__":
    read("src/jobs.csv")
