from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        path_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = path_reader
        table = []
        for row in data:
            # ..source: https://www.w3schools.com/python/ref_func_zip.asp
            collection = zip(header, row)
            table.append(dict(collection))
    return table


"""
 the function 'csv.DictReader' could be used here replacing 'csv.reader'
 with it isn't necessary the line 9 and the func zip
 as it can be see here:
 https://github.com/tryber/sd-011-project-job-insights/blob/tarcisio-menezes-job-insights/src/jobs.py
 as complement he add a 'try/except' for occasions where the file not exist

 or, in a pythonic way the 'csv.reader' and the line 9 could be sustained
 plus the use of 'List Comprehension'
 as used here:
 https://github.com/tryber/sd-011-project-job-insights/blob/luiz-wendel-job-insights-project/src/jobs.py

"""
