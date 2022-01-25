from functools import lru_cache
import csv


@lru_cache
def read(path):
    result = []
    with open(path, encoding="utf8", newline="") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_reader:
            result.append(job)

    return result


if __name__ == "__main__":
    print(read("src/jobs.csv")[0])
