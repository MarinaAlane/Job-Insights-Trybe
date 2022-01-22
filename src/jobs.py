from functools import lru_cache
import csv


@lru_cache
def read(path):
    openFile = open(path)
    with openFile as file:
        readerJobs = csv.DictReader(file)
        jobsTable = []
        for row in readerJobs:
            jobsTable.append(row)

    return jobsTable
